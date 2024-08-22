'''
1. Use original audio to pad the audio to 1 minutes.
2. This code is used for all audio in dolphin category.
3. All audio in dolphin category is 10 seconds, so they will be padding to 1 minutes by using their original audio.
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from observe_audio_function_ver4 import SAMPLE_RATE, AUDIO_LEN, load_audio, get_mel_spectrogram, plot_mel_spectrogram, denoise
import os 
# Create a directory to store the spectrogram images
source_folder = r"D:\ocean_sound_project\dataset_ver1\dolphin_add_noise20db"
destination_folder = r"D:\ocean_sound_project\dataset_ver1\images\dolphin_add_noise20db_mel_spec"
SEGMENT_LENGTH = AUDIO_LEN * 12 # one segment is 1 minutes, and the original `AUDIO_LEN` is 5 seconds.
# So, SEGEMENT_LENGTH should be considered as 1 minutes.

if __name__ == "__main__":
    os.makedirs(destination_folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)
        audio, sr = load_audio(filepath, sr=SAMPLE_RATE)
        # do the denoise only "on original audio" and "not on the audio data augmentation ones"
        # audio = denoise(audio, sr)
        # pad the audio with the original audio or cut the audio
        # print(filename,len(audio))
        if len(audio) < SEGMENT_LENGTH:
            length_audio = len(audio)
            repeat_count = (SEGMENT_LENGTH + length_audio - 1) // length_audio  # Calculate the `ceiling` of AUDIO_LEN / length_audio
            audio = np.tile(audio, repeat_count)[:SEGMENT_LENGTH]  # Repeat and cut to the required length
        else:
            audio = audio[:SEGMENT_LENGTH]

        spec = get_mel_spectrogram(audio)
        fig = plot_mel_spectrogram(spec)
        plt.title("Mel-Spectrogram", fontsize=17)

        # Save the spectrogram image with a meaningful filename
        # dest_filename = f"bonafide_melspec_{filename[:-4]}.png"  # Use single quotes inside the f-string
        dest_filename = f"{filename[:-4]}_mel_spec.png"  # Use single quotes inside the f-string
        dest_filepath = os.path.join(destination_folder, dest_filename)
        plt.savefig(dest_filepath)
        # Close the figure to free up resources
        plt.close()

    print(f"Spectrogram images saved to {destination_folder}")