from faster_whisper import WhisperModel
def transcribe_audio(input_file):
  model_size = "large-v2"

  # Run on GPU with FP16
  model = WhisperModel(model_size, device="cuda", compute_type="float16")

  # or run on GPU with INT8
  # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
  # or run on CPU with INT8
  # model = WhisperModel(model_size, device="cpu", compute_type="int8")

  segments, info = model.transcribe(input_file, beam_size=5, language="ur")

  print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
  transcription = []
  for segment in segments:
        start_time = segment.start
        end_time = segment.end
        text = segment.text.encode('utf-8').decode('utf-8')
        transcription.append(f"[{start_time:.2f}s -> {end_time:.2f}s] {text}")
  # print(transcription)
  return transcription