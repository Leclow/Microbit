# Imports go at the top
from microbit import *
import radio
radio.config(group=32)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()
    if message:
        if message == 'forward':
            message = radio.receive()
            if message:
                display.scroll(message)
        elif message != 'klax':
            display.show(Image.BUTTERFLY)
