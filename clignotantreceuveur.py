left=False
right=False
while True:
    message = radio.receive()
    if message == 'light':
        left=not left
    if message == 'disco':
        right=not right

    moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
    while left ==True:
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

    while right ==True:
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

