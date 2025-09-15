from pynput.keyboard import Key, Listener

# Tracks the number of unlock key presses 
unlock_key_count = 0
# Indicates whether the keyboard is currently locked
is_locked = True
# Keyboard listener instance
keyboard_listener = None

def on_key_press(key):
    """
    Handles key press events. In locked mode, increments unlock_key_count
    when one of the unlock keys (ESC, Backspace, F8) is pressed. Unlocks
    when the count reaches 3.
    """
    global unlock_key_count, is_locked, keyboard_listener
    if is_locked:
        if key in (Key.esc, Key.backspace, Key.f8):
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

