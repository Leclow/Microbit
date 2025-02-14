#recevoir

from microbit import *
import radio
radio.config(group=32)
radio.on()
while True:
    message = radio.receive()
    if message:
        if message == 'hello':
            display.scroll(message)

#envoyer

from microbit import *
import radio
radio.config(group=32)
radio.on()
while True:
    if button_a.is_pressed():
        radio.send('hello')
    
        