from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import re

app = Flask(__name__)

cpp_process = None
output_lines = []

# Thread-safe output buffer
lock = threading.Lock()

# filter the terminal color code
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def run_cpp():
    global cpp_process
    global output_lines

    cpp_process = subprocess.Popen(
        [r"D:\ocean_sound_project\flask_web_src_v1\test.exe"],  # abs path
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    with cpp_process.stdout:
        for line in iter(cpp_process.stdout.readline, ''):
            with lock:
                output_lines.append(line.strip())

    cpp_process.wait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global output_lines
    global cpp_process
    if cpp_process is None or cpp_process.poll() is not None:
        end_process()  # just to be safe
        output_lines = []
        threading.Thread(target=run_cpp, daemon=True).start()
        return jsonify({'status': 'started'})
    else:
        return jsonify({'status': 'already running'})

# end the program
@app.route('/stop', methods=['POST'])
def stop():
    end_process()
    return jsonify({'status': 'stopped'})
# end the program and clear the window
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
            if clean_line.startswith("The prediction is"):
                matched.append(clean_line)
        output_lines.clear() # after post one output to front end, clear this list
        return jsonify({'output': matched})

        # return jsonify({'output': output_lines[-20:]})  # 回傳最近 20 行
def end_process():
    global cpp_process, output_lines

    with lock:
        if cpp_process and cpp_process.poll() is None:
            cpp_process.terminate()
            cpp_process.wait(timeout=2)
        cpp_process = None
        output_lines.clear()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
