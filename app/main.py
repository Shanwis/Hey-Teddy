from config import BUFFER_SIZE
from recognizer import recognizer, stream, porcupine
from commands import commands
import json
import struct

print("Teddy activated.....")

while True:
    frame = stream.read(porcupine.frame_length, exception_on_overflow=False)
    pcm = struct.unpack_from("h" * porcupine.frame_length, frame)

    if porcupine.process(pcm) >= 0:
        print("Teddy is listening.....")

        while True:
            data = stream.read(BUFFER_SIZE, exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                command = result["text"].strip().lower()

                print("Command:",command)

                if(command in commands.keys()):
                    commands[command]()
                    print("Executed:",command)
                    break
                elif(command == 'cancel'):
                    break