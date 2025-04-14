from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import re
import os
import signal

app = Flask(__name__)

cpp_process = None
output_lines = []
lock = threading.Lock()

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def run_cpp():
    global cpp_process, output_lines

    try:
        cpp_process = subprocess.Popen(
            [r"/root/DNN/chou_tf_model_no_batchnorm_ver2/run/run.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            preexec_fn=os.setsid
        )

        with cpp_process.stdout:
            for line in iter(cpp_process.stdout.readline, ''):
                with lock:
                    output_lines.append(line.strip())

        # 等待子進程完全退出（如果還在）
        if cpp_process and cpp_process.poll() is None:
            try:
                cpp_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                print("[run_cpp] Wait timeout after process finished unexpectedly.")
    except Exception as e:
        print(f"[run_cpp] Exception: {e}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global cpp_process, output_lines
    if cpp_process is None or cpp_process.poll() is not None:
        end_process()
        output_lines = []
        threading.Thread(target=run_cpp, daemon=True).start()
        return jsonify({'status': 'started'})
    return jsonify({'status': 'already running'})

@app.route('/stop', methods=['POST'])
def stop():
    end_process()
    return jsonify({'status': 'stopped'})

@app.route('/reset', methods=['POST'])
def reset():
    end_process()
    return jsonify({'status': 'reset'})

@app.route('/output', methods=['GET'])
def output():
    with lock:
        matched = []
        for line in output_lines[-20:]:
            clean_line = ansi_escape.sub('', line)
            # print(clean_line)
            if clean_line.startswith("The prediction is") or clean_line.startswith("output result"):
                matched.append(clean_line)
        output_lines.clear()
        return jsonify({'output': matched})

def end_process():
    global cpp_process, output_lines
    with lock:
        if cpp_process and cpp_process.poll() is None:
            try:
                os.killpg(os.getpgid(cpp_process.pid), signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                cpp_process.wait(timeout=2)
            except Exception as e:
                print(f"[end_process] Error waiting for process: {e}")
        cpp_process = None
        output_lines.clear()


if __name__ == '__main__':
    app.run(host='140.117.176.40', port=5000, debug=True)
