from config import BUFFER_SIZE
from recognizer import recognizer, stream, porcupine
from commands import commands
from nlu import detect_intent
from single_instance import set_instance,cleanup
from tts import speak
from responses import get_response
import json
import struct
import time

set_instance()
print("Teddy is running now.....")
time.sleep(0.1)
speak("Hello, for my assistance just say the magic phrase")

while True:
    frame = stream.read(porcupine.frame_length, exception_on_overflow=False)
    pcm = struct.unpack_from("h" * porcupine.frame_length, frame)

    if porcupine.process(pcm) >= 0:
        speak(get_response("listening"))
        print("Teddy is listening.....")

        while True:
            data = stream.read(BUFFER_SIZE, exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                command = result["text"].strip().lower()

                print("Command:",command)        
                intent = detect_intent(command)

                if intent in commands.keys():
                    speak(get_response(intent))
                    commands[intent]()
                    break
                elif(intent == 'cancel'):
                    speak(get_response("cancel"))
                    break
                else:
                    res = get_response("unknown")
                    speak(res)
                    time.sleep(0.2 + len(res) * 0.05)  # Adjust sleep time based on command length

                
