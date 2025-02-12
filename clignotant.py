# Imports go at the top
from microbit import *
import radio
radio.config(group=69)
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

#def on_forever():
#    global moveMotorZIP2
#    moveMotorZIP2 = Kitronik_Move_Motor.create_move_motor_zipled(4)
#    moveMotorZIP2.set_zip_led_color(0,
#        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
#    basic.pause(50)
#   moveMotorZIP2.set_zip_led_color(1,
#        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
#    basic.pause(50)
#    moveMotorZIP2.set_zip_led_color(2,
#        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
#    basic.pause(50)
#    moveMotorZIP2.set_zip_led_color(3,
#        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
#    basic.pause(50)
#basic.forever(on_forever)
