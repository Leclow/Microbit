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




# New main
radio.set_group(32)

def on_received_string(receivedString):
    if receivedString == 'FORWARD':
        radio.on_received_number(movementControl)
    elif receivedString == 'light':
        radio.on_received_string(lightControl)



def movementControl(receivedNumber):
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, receivedNumber)

def on_received_number(receivedNumber):
    return receivedNumber


def lightControl(light):
    if light == "left":
        while left == "left":
            moveMotorZIP.set_zip_led_color(0,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
            moveMotorZIP.set_zip_led_color(3,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
            moveMotorZIP.show()
            basic.pause(500)
            moveMotorZIP.set_zip_led_color(0,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.set_zip_led_color(3,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.show()
            basic.pause(500)
    elif light == "right":
        while light == "right":
            moveMotorZIP.set_zip_led_color(1,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
            moveMotorZIP.set_zip_led_color(2,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
            moveMotorZIP.show()    
            basic.pause(500)
            moveMotorZIP.set_zip_led_color(1,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.set_zip_led_color(2,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.show()    
            basic.pause(500)

while True:
    radio.on_received_string(on_received_string)

# test
radio.set_group(32)
moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)

def on_received_string(receivedString):
    if receivedString == 'FORWARD':
        radio.on_received_number(movementControl)
    elif receivedString == 'light':
        radio.on_received_string(lightControl)



def movementControl(receivedNumber):
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, receivedNumber)

def on_received_number(receivedNumber):
    return receivedNumber


def lightControl(receivedString):    
    if receivedString == "left":
        while receivedString == "left":
            moveMotorZIP.set_zip_led_color(0,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
            moveMotorZIP.set_zip_led_color(3,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
            moveMotorZIP.show()
            basic.pause(500)
            moveMotorZIP.set_zip_led_color(0,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.set_zip_led_color(3,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.show()
            basic.pause(500)
    elif receivedString == "right":
        while receivedString == "right":
            moveMotorZIP.set_zip_led_color(1,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
            moveMotorZIP.set_zip_led_color(2,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
            moveMotorZIP.show()
            basic.pause(500)
            moveMotorZIP.set_zip_led_color(1,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.set_zip_led_color(2,
                Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
            moveMotorZIP.show()
            basic.pause(500)

while True:
    radio.on_received_string(lightControl)





