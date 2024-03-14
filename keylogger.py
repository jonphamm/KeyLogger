from pynput import keyboard

def on_press(key):
    try:
        #Printing the key that was pressed
        print(f'Key {key.char} pressed')
    except AttributeError:
        #Handling special keys
        print(f'Special key {key} pressed')

def on_release(key):
    #Exiting the program when the 'esc' key is pressed
    if key == keyboard.Key.esc:
        print('Exiting program')
        return False
    
#Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #Running the listener in the background
    listener.join()