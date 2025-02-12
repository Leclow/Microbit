from microbit import *
import music
import radio
radio.config(group=32)
radio.on()

while True:
    if pin_logo.is_touched():
        radio.send('klax')
        display.show(Image('00300:'
                           '03630:'
                           '36963:'
                           '03630:'
                           '00300'))
    

            
    
       