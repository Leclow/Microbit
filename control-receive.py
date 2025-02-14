# Imports go at the top
from microbit import *
import radio
radio.config(group=32)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    direction = radio.receive()
    if direction:
        if direction == 'forward':
            speed = radio.receive()
            if speed:
                Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, int(speed))

        elif message != 'klax':
            display.show(Image.BUTTERFLY)
