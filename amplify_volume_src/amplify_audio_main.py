import numpy as np
from amplify_audio_func import load_audio, amplify_audio, save_audio, get_max_factor
import os
source_dir = r"D:\ocean_sound_project\original_dataset_with_label_name\Merge_sound\船+魚"
dest_dir = r"D:\ocean_sound_project\original_dataset_with_label_name\Merge_sound\merge_sound_amplify\boat_fish_amplify"
FACTOR = 4 # factor to amplify this audio

if __name__ == "__main__":
    for audio_file in os.listdir(source_dir):
        FACTOR = 4
        file_path = os.path.join(source_dir, audio_file)
        # Load the audio
        audio, sr = load_audio(file_path)
        max_amplitude = np.max(np.abs(audio))
        print(f"max_amplitude {audio_file} audio has: {max_amplitude}")
        max_factor = get_max_factor(audio)
        print(f"max_factor {audio_file} audio can be amplified: {max_factor}")
        if(max_factor < FACTOR):
            FACTOR = round(max_factor * 0.8)
            print(f"Warning: {audio_file} exceed the setting factor, so resetting the factor as 80% of acceptable factor: {FACTOR}")
        
        dest_file_name = f"{audio_file[:-4]}_f{FACTOR}.wav"
        dest_file_path = os.path.join(dest_dir, dest_file_name)

        # Amplify the audio
        amplified_audio = amplify_audio(audio, factor=FACTOR)  # Increase volume by 2x

        # Save the amplified audio
        save_audio(amplified_audio, dest_file_path)

        print(f"Amplified audio saved to: {dest_file_path}")