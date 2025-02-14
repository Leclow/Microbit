# Imports go at the top
from microbit import *
import radio
radio.config(group=32)
radio.on()

while True:
    if button_a.was_pressed():
        radio.send('light')
        display.scroll('A')
    if button_b.was_pressed():
        radio.send('disco')
        display.scroll('B')
    while True:
        message = radio.receive()
        if message == 'light':

        if message == 'disco':
