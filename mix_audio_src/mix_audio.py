from pydub import AudioSegment

def match_length(sound1, sound2):
    # 找出兩個音檔的最大長度
    length1 = len(sound1)
    length2 = len(sound2)
    
    if length1 == length2:
        return sound1, sound2
    
    # 如果音檔1較短，則將它重複直到與音檔2的長度相同，反之亦然
    if length1 < length2:
        sound1 = (sound1 * (length2 // length1)) + sound1[:length2 % length1]
    else:
        sound2 = (sound2 * (length1 // length2)) + sound2[:length1 % length2]
    
    return sound1, sound2

def mix_audio_wav(path1, path2, dest_path):
    # 加載音檔
    sound1 = AudioSegment.from_file(path1)
    sound2 = AudioSegment.from_file(path2)

    # 匹配音檔長度
    sound1, sound2 = match_length(sound1, sound2)

    # 疊合兩個音檔
    combined = sound1.overlay(sound2)

    # 保存混合後的音檔
    combined.export(dest_path, format="wav")


def mix_audio_wav_gaindb_path2(path1, path2, dest_path, gain_db=0):
    # 加載音檔
    sound1 = AudioSegment.from_file(path1)
    sound2 = AudioSegment.from_file(path2)

    # 調整第二個音檔的音量（根據 gain_db 調整，默認為不變）
    sound2 = sound2 + gain_db  # 將音量增加 gain_db 分貝

    # 匹配音檔長度
    sound1, sound2 = match_length(sound1, sound2)

    # 疊合兩個音檔
    combined = sound1.overlay(sound2)

    # 保存混合後的音檔
    combined.export(dest_path, format="wav")