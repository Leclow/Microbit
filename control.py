from microbit import *


while True:
    x_strength = accelerometer.get_x()
    y_strength = accelerometer.get_y()
    minimalX = 250
    minimalY = 250
    if x_strength > minimalX:
        display.show("D")
    elif x_strength < -minimalX:
        display.show("G")
    elif y_strength > minimalY:
        display.show("H")
    elif y_strength < -minimalY:
        display.show("B")
    else:
        display.show("-")
