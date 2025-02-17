def on_forever():
    Kitronik_Move_Motor.set_ultrasonic_units(Kitronik_Move_Motor.Units.CENTIMETERS)
    if Kitronik_Move_Motor.measure() < 10:
        Kitronik_Move_Motor.stop()
        basic.pause(100)
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE, 35)
        basic.pause(500)
basic.forever(on_forever)
