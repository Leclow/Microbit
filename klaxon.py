from microbit import *
import music
import radio
radio.config(group=32)
radio.on()
while True:
    message = radio.receive()
    if message == 'klax':
        music.pitch(440, duration=-1)
        display.scroll('ok')# Émettre un son continu de 440 Hz
    else:
        music.stop()


#envoyer
from microbit import *
import music
import radio
radio.config(group=32)
radio.on()

while True:
    if pin_logo.is_touched():
        radio.send('klax')
        display.scroll('k')
        sleep(1000)
        display.clear()

 
    
        
    

            
    
       