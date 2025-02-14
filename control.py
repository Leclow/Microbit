# Imports go at the top
from microbit import *
import radio
radio.config(group=32)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    x_strength = accelerometer.get_x()
    y_strength = accelerometer.get_y()
    minimalX = 250
    minimalY = 250
    if x_strength > minimalX:
        display.show("D")
        # need to send with radio the direction and the speed calculated
        radio.send('forward')
        radio.send('1')
    elif x_strength < -minimalX:
        display.show("G")
    elif y_strength > minimalY:
        display.show("H")
    elif y_strength < -minimalY:
        display.show("B")
    else:
        display.show("-")
