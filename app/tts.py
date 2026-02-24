import pyaudio
from piper import PiperVoice

voice = PiperVoice.load("models/en_US-ryan-medium.onnx")

pa = pyaudio.PyAudio()
stream = None

def speak(text):
    global stream

    for chunk in voice.synthesize(text):
        if stream is None:
            stream = pa.open(
                format=pyaudio.paInt16,
                channels=chunk.sample_channels,
                rate=chunk.sample_rate,
                output=True,
                frames_per_buffer=1024
            )

        stream.write(chunk.audio_int16_bytes)

def close_audio():
    global stream
    if stream is not None:
        stream.stop_stream()
        stream.close()
        stream = None
    pa.terminate()