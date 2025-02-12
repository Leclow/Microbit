from microbit import *
import music
import radio
radio.config(group=32)
radio.on()

while True:
    message = radio.receive()
    if message:
        if message == 'klax':
            display.show(Image.HEART)
            speaker.on()
            music.pitch(440)
        elif message != 'klax':
            display.show(Image.BUTTERFLY)
            speaker.stop()