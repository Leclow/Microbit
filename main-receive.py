# important stuff
from microbit import *
import radio
import music
radio.config(group=32)
radio.on()

# functions
def movementControl(direction, speed):
    display.scroll(direction, speed)

def lightControl(light):
    display.scroll(light)

while True
    message = radio.receive()
    if message:
        if message == "control":
            direction = radio.receive()
            if direction:
                speed = radio.receive()
                if speed:
                    movementControl(direction, speed)

        elif message == "light":
            light = radio.receive()
            if light:
                lightControl(light)

        elif message == "klaxon":
            while message == "klaxon":
                speaker.on()
                music.pitch(440)
          speaker.stop()

        elif message == "random func":
            display.scroll("random")