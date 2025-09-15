from pynput.keyboard import Key, Listener
import os

# Tracks the number of unlock key presses 
unlock_key_count = 0
# Indicates whether the keyboard is currently locked
is_locked = True
# Keyboard listener instance
keyboard_listener = None

# Path to unlock keys file
KEYS_FILE = os.path.join(os.path.dirname(__file__), 'code-keys.txt')


# Dynamically map key names to pynput Key objects
def key_name_to_key(key_name):
    try:
        return getattr(Key, key_name)
    except AttributeError:
        return None

def load_unlock_keys():
    """
    Reads unlock key names from code-keys.txt and returns a set of Key objects.
    Allows any valid Key attribute from pynput.keyboard.Key.
    """
    unlock_keys = set()
    try:
        with open(KEYS_FILE, 'r') as f:
            for line in f:
                key_name = line.strip().lower()
                key_obj = key_name_to_key(key_name)
                if key_obj:
                    unlock_keys.add(key_obj)
    except Exception:
        pass  # If file missing or error, fallback to default
    if not unlock_keys:
        # Default keys if file is empty or missing
        unlock_keys = {Key.esc, Key.backspace, Key.f8}
    return unlock_keys

UNLOCK_KEYS = load_unlock_keys()

def on_key_press(key):
    """
    Handles key press events. In locked mode, increments unlock_key_count
    when one of the unlock keys (from code-keys.txt) is pressed. Unlocks
    when the count reaches 3.
    """
    global unlock_key_count, is_locked, keyboard_listener
    if is_locked:
        if key in UNLOCK_KEYS:
            unlock_key_count += 1
        # Ignore all other keys while locked

    # Unlock if required number of keys pressed
    if unlock_key_count >= 3:
        is_locked = False
        unlock_key_count = 0
        keyboard_listener.stop()

def start_keyboard_listener(suppress_keys):
    """
    Starts the keyboard listener. If suppress_keys is True, all keys are suppressed.
    """
    global keyboard_listener
    keyboard_listener = Listener(on_press=on_key_press, suppress=suppress_keys)
    keyboard_listener.start()
    keyboard_listener.join()

# Start with keyboard locked and keys suppressed
start_keyboard_listener(suppress_keys=True)

# After unlocking, start listener without suppression
if not is_locked:
    start_keyboard_listener(suppress_keys=False)

