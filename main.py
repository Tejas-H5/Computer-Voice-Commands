import speech_recognition as sr
import pyautogui
import time
import asyncio
 
print("Program starting...")

r = sr.Recognizer()

print("Program started. Try saying something")

# globals

is_typing = True
default_delay = 0.01

# functions


# TODO: try vosk library, see if its better/faster

def main_loop():
    while(1):   
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                
                my_text = r.recognize_google(audio)
                my_text = my_text.lower()
                
                handle_command(my_text)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")

punctuation_map = {
    "space": " ",
    "period": ".",
    "full stop": ".",
    "forward slash": "/",
    "backslash": "\\",
    "comma": ",",
    "quote": "\"",
    "double quote": "\"",
    "single quote": "'",
    "colon": ":",
    "semicolon": ";",
    "vertical bar": "|",
    "add": "+",
    "subtract": "-",
    "times": "*",
    "divide": "/",
    "equals": "=",
    "exclamation": "!",
    "exclaim": "!",
    "backtick": "`",
    "tilde": "~",
    "at": "@",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "hat": "^",
    "ampersand": "&",
    "asterisk": "*",
    # brackets
    "open bracket": "(",
    "close bracket": ")",
    "open square bracket": "[",
    "close square bracket": "]",
    "open angle bracket": "<",
    "close angle bracket": ">",
    "open brace": "{",
    "close brace": "}",
    # copy paste brackets above, and multi-edit open -> opening, close -> closing
    "opening bracket": "(",
    "closing bracket": ")",
    "opening square bracket": "[",
    "closing square bracket": "]",
    "opening angle bracket": "<",
    "closing angle bracket": ">",
    "opening brace": "{",
    "closing brace": "}",
    # end copy paste
}

sequence_map = {
    "undo": [["ctrl", "z"]],
    "anju": [["ctrl", "z"]],
    "revert": [["ctrl", "z"]],
    "redo": [["ctrl", "y"]],
    "backspace": [["backspace"]],
    "tab": [["tab"]],
    "enter": [["enter"]],
    "new line": [["enter"]],
    "escape": [["escape"]],
    "backspace word": [["ctrl", "backspace"]],
    "delete": [["delete"]],
    "delete word": [["ctrl", "delete"]],
    "bold": [["ctrl", "b"]],
    "italic": [["ctrl", "b"]],
}

#TODO: vim-like commands
# up, down, left, right
# number to multiply the previous command
# select line
# select up
# start of line
# end of line


def handle_command(text):
    """ This dispatches text to pyautogui or whatever as fast as possible.
This method must not block the main thread for any large amount of time, as that
will prevent the main thread from listening to what is being said next, unless it makes sense to block
like with hotkeys and such
"""

    global is_typing

    # if the command is like backspace words 40, we want backspace words to be the text, and 40 to 
    # be the number of times the command is repeated
    repeats = 1
    try:
        text_words = text.split(' ')
        repeats = int(text_words[-1])
        text = ' '.join(text_words[:-1])
    except Exception as e:
        print(e)
        pass

    if is_typing:
        if text == "stop typing":
            is_typing = False
        elif text in punctuation_map:
            send_keyboard_input_async(punctuation_map[text])
        elif text in sequence_map:
            print("Executing sequence for the", text, "command:")

            # should be blocking
            sequence = sequence_map[text]

            for i in range(repeats):
                for hotkeys in sequence:
                    print("Sending hotkeys:", " + ".join(hotkeys))
                    pyautogui.hotkey(*hotkeys)
        else:
            send_keyboard_input_async(text)
    else:
        print("Got text: ", text)
        if text == "start typing":
            is_typing = True


def send_keyboard_input_async(text, delay = default_delay):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(send_keyboard_input(text, delay = delay))

async def send_keyboard_input(text, delay = default_delay):
    print("Sending to keyboard: '", text, "'")

    pyautogui.typewrite(text, interval=delay)

main_loop()

# # testing
# delay = 1.5
# print("testing in ", delay)
# time.sleep(delay)
# print("testing ...")
# handle_command("backspace word 50")