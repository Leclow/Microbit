    Kitronik_Move_Motor.set_ultrasonic_units(Kitronik_Move_Motor.Units.CENTIMETERS)
    if Kitronik_Move_Motor.measure() < 10:
        Kitronik_Move_Motor.stop()
        basic.pause(100)
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE, 10)
        basic.pause(1500)
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.LEFT, 10)
        basic.pause(1500)
basic.forever(on_forever)
