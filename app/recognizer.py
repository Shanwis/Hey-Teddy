from vosk import Model, KaldiRecognizer
from config import SAMPLE_RATE
import pyaudio

model = Model(r"models/vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model,SAMPLE_RATE)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, input=True, frames_per_buffer=8192)

stream.start_stream()


