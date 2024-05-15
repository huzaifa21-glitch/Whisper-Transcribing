import librosa
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub import AudioSegment
from pydub.silence import split_on_silence
import time
import json
from faster_whisper import WhisperModel
import librosa
import numpy as np
from scipy.io.wavfile import write
def process_audio(input_file):
    decibel_level = 35
    # Remove silence
    output_file_silence_removed = "output_silence_removed.wav"
    silent_spots_info = remove_silence(input_file, output_file_silence_removed)
    silent_spots_count = json.loads(silent_spots_info)["Total silent spots"]

    # Enhance audio
    output_file_enhanced = "output_enhanced.wav"
    adjust_decibel_level(output_file_silence_removed, decibel_level, output_file_enhanced)

    # Transcribe audio
    transcription = transcribe_audio(output_file_enhanced)
    # print(transcription)

    # Return silent spots count and transcription in JSON format
    output = json.dumps({"Total silent spots": silent_spots_count, "Transcription": transcription}, ensure_ascii=False)
    return output

input_file = "/content/drive/MyDrive/audio3.wav"
output = process_audio(input_file)
print('JSON: '+output)