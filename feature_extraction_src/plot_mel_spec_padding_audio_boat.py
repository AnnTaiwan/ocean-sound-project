'''
1. Use original audio to pad the audio to 1 minutes.
2. This code is used for all audio in boat category.
3. All audio in boat category is 10 minutes, so they will be chopped into 10 segemnts.
'''
import matplotlib.pyplot as plt
from observe_audio_function_ver4 import SAMPLE_RATE, AUDIO_LEN, load_audio, get_mel_spectrogram, plot_mel_spectrogram, denoise
import os 
# Create a directory to store the spectrogram images
source_folder = r"D:\ocean_sound_project\original_dataset_with_label_name\Z_split1\boat_val"
destination_folder = r"D:\ocean_sound_project\mix_dataset_ver2\IMAGES\boat_val_mel_spec"
destination_folder2 = r"D:\ocean_sound_project\mix_dataset_ver2\IMAGES\Z_final_dataset_1\val"

SEGMENT_LENGTH = AUDIO_LEN * 12 # one segment is 1 minutes, and the original `AUDIO_LEN` is 5 seconds.
# So, SEGEMENT_LENGTH should be considered as 1 minutes.

if __name__ == "__main__":
    os.makedirs(destination_folder, exist_ok=True)
    count = 0
    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)
        audio, sr = load_audio(filepath, sr=SAMPLE_RATE)
        # do the denoise only "on original audio" and "not on the audio data augmentation ones"
        audio = denoise(audio, sr)
        # pad the audio with the original audio or cut the audio
        

        # Check the length of the audio
        total_length = len(audio)
        num_segments = total_length // SEGMENT_LENGTH  # Calculate the number of 1-minute segments
        count += 1
        print(f"[{count}] : ", filename,total_length, num_segments) # like boat_M1_20201016_120407.wav 28800001 10
        # Process each 1-minute segment of the audio
        for i in range(num_segments):
            start_sample = i * SEGMENT_LENGTH
            end_sample = (i + 1) * SEGMENT_LENGTH
            audio_segment = audio[start_sample:end_sample]

            spec = get_mel_spectrogram(audio_segment)
            fig = plot_mel_spectrogram(spec)
            plt.title("Mel-Spectrogram", fontsize=17)

            # Save the spectrogram image with a meaningful filename
            # dest_filename = f"bonafide_melspec_{filename[:-4]}.png"  # Use single quotes inside the f-string
            dest_filename = f"{filename[:-4]}_segment_{i+1}_mel_spec.png"  # Use single quotes inside the f-string
            dest_filepath = os.path.join(destination_folder, dest_filename)
            dest_filepath2 = os.path.join(destination_folder2, dest_filename)
            plt.savefig(dest_filepath)
            plt.savefig(dest_filepath2)
            # Close the figure to free up resources
            plt.close()

    print(f"Spectrogram images saved to {destination_folder}")