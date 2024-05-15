import librosa
import numpy as np
from scipy.io.wavfile import write
# import noisereduce

def adjust_decibel_level(file_path, decibel_level, output_file):
    # Load audio file
    audio, sample_rate = librosa.load(file_path)

    # Normalize audio
    audio = librosa.util.normalize(audio, axis=0)

    # Adjust decibel level
    audio = audio * (1 + (decibel_level / 100))

    # Remove background noise using noisereduce
    # audio = noisereduce.reduce_noise(audio)

    # Clip audio to valid range
    audio = np.clip(audio, -1, 1)

    # Write output file
    write(output_file, sample_rate, audio)

# Example usage:
input_file = './audios/silent_output.wav'
output_file = './audios/silent_output2.wav'
decibel_level = 35  # adjust this value to your liking
adjust_decibel_level(input_file, decibel_level, output_file)