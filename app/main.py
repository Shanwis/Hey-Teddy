from config import BUFFER_SIZE, WAKE_WORD
from recognizer import recognizer, stream
from commands import commands
import json

while True:
    data = stream.read(BUFFER_SIZE, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result["text"]
        print("Heard:",text)
        if(text.startswith(WAKE_WORD)):
            command = text.replace(WAKE_WORD,"").strip()
            if(command in commands.keys()):
                commands[command]()
                print("Executed:",command)
        