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

def on_received_value(name, value):
    global autopilot
    if name == "s":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 0)
    elif name == "l":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.LEFT, (value - 824) / 2)
    elif name == "b":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE,
            (value * -1 + 200) / 2)
    elif name == "r":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.RIGHT,
            (value * -1 + 200) / 2)
    elif name == "ll":
        lightleft2()
    elif name == "lr":
        lightright2()
    elif name == "f":
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD,
            (value - 824) / 2)
    elif name == "k":
        Kitronik_Move_Motor.beep_horn()
    elif name == "trump":
        Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
            Kitronik_Move_Motor.MotorDirection.FORWARD,
            100)
        Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
            Kitronik_Move_Motor.MotorDirection.REVERSE,
            100)
    elif name == "c":
        autopilot = not (autopilot)
radio.on_received_value(on_received_value)

def lightleft2():
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
autopilot = False
moveMotorZIP: Kitronik_Move_Motor.MoveMotorZIP = None
radio.set_group(44)
moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
Kitronik_Move_Motor.turn_radius(Kitronik_Move_Motor.TurnRadii.TIGHT)
autopilot = False
moveMotorZIP.set_zip_led_color(0,
    Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
moveMotorZIP.set_zip_led_color(1,
    Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
moveMotorZIP.set_zip_led_color(2,
    Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
moveMotorZIP.set_zip_led_color(3,
    Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))

def on_forever():
    if autopilot:
        Kitronik_Move_Motor.set_ultrasonic_units(Kitronik_Move_Motor.Units.CENTIMETERS)
        if Kitronik_Move_Motor.measure() < 20:
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE, 10)
basic.forever(on_forever)
