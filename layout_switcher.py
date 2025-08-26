from pynput import keyboard
import pyperclip
import change_lang
import time

controller = keyboard.Controller()

is_active = False

def on_activate():
    global is_active
    if is_active:
        return
    is_active = True

    activ_buffer = pyperclip.paste()

    pyperclip.copy('__EMPTY__')
    with controller.pressed(keyboard.Key.cmd):
        controller.tap('c')

    time.sleep(0.3)

    after =  pyperclip.paste()

    if after == '__EMPTY__' or after == '':
        pyperclip.copy(activ_buffer)
    else:
        change_word = pyperclip.paste()
        changed_string = change_lang.replace_letter(change_word)
        pyperclip.copy(changed_string)

        with controller.pressed(keyboard.Key.cmd):
            controller.tap('v')

        time.sleep(0.3)

    pyperclip.copy(activ_buffer)

    is_active = False


def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<cmd>+<ctrl>'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()