import os
from mix_audio import mix_audio_wav, mix_audio_wav_amplify, mix_audio_wav_amplify_two
FACTOR = 4
if __name__ == "__main__":
    source_dir1 = r"D:\ocean_sound_project\original_dataset_with_label_name\boat_add_noise20db"
    source_dir2 = r"D:\ocean_sound_project\original_dataset_with_label_name\whale_add_noise20db"

    dest_dir = r"D:\ocean_sound_project\mix_dataset_ver1\boat_whale_add_noise20db"
    os.makedirs(dest_dir, exist_ok=True)

    for file1 in os.listdir(source_dir1):
        path1 = os.path.join(source_dir1, file1)
        
        # Ensure file1 is a .wav file
        if not file1.endswith(".wav"):
            continue
        
        for file2 in os.listdir(source_dir2):
            path2 = os.path.join(source_dir2, file2)

            # Ensure file2 is a .wav file
            if not file2.endswith(".wav"):
                continue

            # Remove extension to create a combined filename
            filename1 = file1.replace(".wav", "")  
            filename2 = file2.replace(".wav", "")

            # Generate the destination file path
            combined_filename = f"{filename1}_{filename2}.wav"
            dest_path = os.path.join(dest_dir, combined_filename)

            # print(f"Mixing {file1} and {file2} -> {dest_path}")
            # mix_audio_wav(path1, path2, dest_path)
            # mix_audio_wav_amplify_two(path1, path2, dest_path, FACTOR=FACTOR)
            mix_audio_wav_amplify(path1, path2, dest_path, FACTOR=FACTOR)
    print("All done!\n\tSave audio into ", dest_dir)
