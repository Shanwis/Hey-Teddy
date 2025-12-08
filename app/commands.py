import os

commands = {
    "shutdown":lambda:os.system("shutdown now"),
    "reboot":lambda:os.system("reboot"),
    "logout":lambda:os.system("gnome-session-quit --logout --no-prompt"),
    "lock screen": lambda:os.system("loginctl lock-session"),
    "open terminal":lambda:os.system("gnome-terminal"),
    "open browser":lambda: os.system("brave-browser"),
}