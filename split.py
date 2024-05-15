from pydub import AudioSegment
from pydub.silence import split_on_silence

# Import stereo audio file and check channels
stereo_phone_call = AudioSegment.from_file("audio5.wav")

# Split stereo phone call and check channels
channels = stereo_phone_call.split_to_mono()

# Remove silent spots and save each channel separately
for i, channel in enumerate(channels):
    # Split on silence
    chunks = split_on_silence(channel, min_silence_len=500, silence_thresh=-40)
    
    # Combine non-silent chunks with a 0.5-second pause between them
    non_silent_audio_with_pause = AudioSegment.silent(duration=500)  # 0.5 seconds of silence
    for chunk in chunks:
        non_silent_audio_with_pause += chunk + AudioSegment.silent(duration=500)  # Add the chunk and 0.5 seconds of silence
    
    # Output file path
    output_path = f"output/channel_{i + 1}_with_pause.wav"
    # Export the result
    non_silent_audio_with_pause.export(output_path, format="wav")
