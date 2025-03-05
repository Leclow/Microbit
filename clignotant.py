# Imports go at the top
from microbit import *
import radio
radio.config(group=44)
radio.on()

while True:
    if button_a.was_pressed():
        radio.send('light')
        display.scroll('A')
    if button_b.was_pressed():
        radio.send('disco')
        display.scroll('B')