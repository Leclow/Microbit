def lightright():
    while lightleft2:
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
def lightleft():
    while lightright2:
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

def on_received_string(receivedString):
    global lightleft2, lightright2
    if receivedString == "forward":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 50)
    elif receivedString == "left":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.LEFT, 50)
    elif receivedString == "backward":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE, 50)
    elif receivedString == "right":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.RIGHT, 50)
    elif receivedString == "lightleft":
        lightleft2 = not (lightleft2)
        lightleft()
    elif receivedString == "lightright":
        lightright2 = not (lightright2)
        lightright()
radio.on_received_string(on_received_string)

lightright2 = False
lightleft2 = False
moveMotorZIP: Kitronik_Move_Motor.MoveMotorZIP = None
radio.set_group(44)
moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)

def on_in_background():
    led.plot(0, 0)
    if lightleft2:
        led.plot(1, 0)
        while True:
            lightleft()
    elif lightright2:
        while True:
            lightright()
        led.plot(10, 1)
control.in_background(on_in_background)
