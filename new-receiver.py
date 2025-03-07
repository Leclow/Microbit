def lightright2():
    moveMotorZIP.set_zip_led_color(0,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
    moveMotorZIP.set_zip_led_color(3,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.set_zip_led_color(1,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
    moveMotorZIP.set_zip_led_color(2,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
    moveMotorZIP.show()
    basic.pause(500)
    moveMotorZIP.set_zip_led_color(1,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
    moveMotorZIP.set_zip_led_color(2,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.show()
    basic.pause(500)
def lighteft():
    moveMotorZIP.set_zip_led_color(1,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
    moveMotorZIP.set_zip_led_color(2,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.set_zip_led_color(0,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
    moveMotorZIP.set_zip_led_color(3,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.YELLOW))
    moveMotorZIP.show()
    basic.pause(500)
    moveMotorZIP.set_zip_led_color(0,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
    moveMotorZIP.set_zip_led_color(3,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.show()
    basic.pause(500)

def on_received_value(name, value):
    global lightleft, lightright
    if name == "stop":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 0)
    elif name == "left":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.LEFT, (value - 824) / 2)
    elif name == "backward":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE,
            (value * -1 + 200) / 2)
    elif name == "right":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.RIGHT,
            (value * -1 + 200) / 2)
    elif name == "lightleft":
        lightleft = not (lightleft)
        lighteft()
    elif name == "lightright":
        lightright = not (lightright)
        lightright2()
    elif name == "forward":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD,
            (value - 824) / 2)
radio.on_received_value(on_received_value)

lightleft = False
lightright = False
moveMotorZIP: Kitronik_Move_Motor.MoveMotorZIP = None
radio.set_group(44)
moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
lightright = False
lightleft = False
Kitronik_Move_Motor.turn_radius(Kitronik_Move_Motor.TurnRadii.TIGHT)





#Let's go ca fonctionne