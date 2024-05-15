from pydub import AudioSegment
from pydub import AudioSegment
from pydub.silence import split_on_silence
import time
import json
def remove_silence(input_file, output_file, min_silence_len=1700, silence_thresh=-50):
    print("Loading the audio file...")
    start_time = time.time()  # Start timer

    audio = AudioSegment.from_mp3(input_file)

    print("Splitting the audio based on silence...")
    chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    print("Concatenating non-silent chunks...")
    output = AudioSegment.empty()
    silent_spots_count = 0
    for chunk in chunks:
        if len(chunk) < 1000:  # If the chunk is too short, consider it as silent spot
            silent_spots_count += 1
            output += AudioSegment.silent(duration=1000)  # Replace with 1 second silent spot
        else:
            output += chunk

    print("Exporting the audio without silent parts...")
    output.export(output_file, format="wav")
    end_time = time.time()  # End timer

    print(f"Total execution time Reducing silent: {end_time - start_time:.2f} seconds")

    # Return silent spots count in JSON format
    silent_spots_info = {"Total silent spots": silent_spots_count}
    return json.dumps(silent_spots_info)

remove_silence(f"/content/drive/MyDrive/audio1.wav",f"/content/drive/MyDrive/output/output.wav" )