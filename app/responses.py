import random

RESPONSES = {
    "shutdown": [
        "Okay, shutting down.",
        "Powering off now.",
        "Turning the system off."
    ],

    "reboot": [
        "Restarting now.",
        "Rebooting the system.",
        "Okay, restarting."
    ],

    "logout": [
        "Logging you out.",
        "Signing out now.",
        "Okay, ending your session."
    ],

    "lock": [
        "Locking the screen.",
        "Securing your session.",
        "Screen locked."
    ],

    "open_terminal": [
        "Opening terminal.",
        "Launching terminal.",
        "Terminal coming up."
    ],

    "open_browser": [
        "Opening your browser.",
        "Launching the browser.",
        "Browser coming up."
    ],

    "open_editor": [
        "Opening your editor.",
        "Launching VS Code.",
        "Starting the code editor."
    ],

    "close_window": [
        "Closing the window.",
        "Okay, closing it.",
        "Window closed."
    ],

    "mute_speaker": [
        "Muting speakers.",
        "Sound off.",
        "Speakers muted."
    ],

    "unmute_speaker": [
        "Unmuting speakers.",
        "Sound back on.",
        "Speakers unmuted."
    ],

    "volume_up": [
        "Turning volume up.",
        "Increasing volume.",
        "Volume raised."
    ],

    "volume_down": [
        "Turning volume down.",
        "Decreasing volume.",
        "Volume lowered."
    ],

    "brightness_up": [
        "Increasing brightness.",
        "Brightening the screen.",
        "Screen brightness up."
    ],

    "brightness_down": [
        "Reducing brightness.",
        "Dimming the screen.",
        "Screen brightness down."
    ],

    "wifi_off": [
        "Turning Wi-Fi off.",
        "Disconnecting from network.",
        "Wi-Fi disabled."
    ],

    "wifi_on": [
        "Turning Wi-Fi on.",
        "Connecting to network.",
        "Wi-Fi enabled."
    ],

    "bluetooth_off": [
        "Turning Bluetooth off.",
        "Bluetooth disabled.",
        "Okay, Bluetooth off."
    ],

    "bluetooth_on": [
        "Turning Bluetooth on.",
        "Bluetooth enabled.",
        "Okay, Bluetooth on."
    ],

    "battery_status": [
        "Checking battery.",
        "Let me see the battery level.",
        "Here's your battery status."
    ],

    "joke": [
        "Alright, here's one.",
        "Okay, listen to this.",
        "Here comes a joke."
    ],

    "cancel": [
        "Okay, cancelled.",
        "Alright, never mind.",
        "No problem."
    ],

    "stop_assistant": [
        "Okay, see you later.",
        "Goodbye for now.",
        "Shutting down Teddy."
    ],

    "unknown": [
        "I didn't catch that.",
        "You there?",
        "Listening!",
        "Are you saying something?"
    ],

    "listening": [
        "Yes?",
        "I'm listening.",
        "Go ahead."
    ],

}

def get_response(intent):
    if intent in RESPONSES:
        return random.choice(RESPONSES[intent])
    else:
        return random.choice(RESPONSES["unknown"])