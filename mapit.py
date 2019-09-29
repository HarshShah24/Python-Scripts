#! python3

import webbrowser,pyperclip,sys

if len(sys.argv) > 1:
    arg = sys.argv
    address = ''.join(arg[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
