def on_button_pressed_a():
    radio.send_value("lightleft", 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("lightright", 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(44)
# ATTENTION : Ne pas oublier d'inclure l'extension BitCommander dans MakeCode !
while True:
    x = bitcommander.read_joystick(BCJoystick.X)
    # Valeur entre 0 et 1024
    y = bitcommander.read_joystick(BCJoystick.Y)
    # Valeur entre 0 et 1024
    d = bitcommander.read_dial()
    # Valeur entre 0 et 630
    t = bitcommander.read_button(BCButtons.JOYSTICK)
    # Valeur True ou False
    r = bitcommander.read_button(BCButtons.RED)
    # Valeur True ou False
    j = bitcommander.read_button(BCButtons.YELLOW)
    # Valeur True ou False
    b = bitcommander.read_button(BCButtons.BLUE)
    # Valeur True ou False
    v = bitcommander.read_button(BCButtons.GREEN)
    print("x=" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + str(x)))))))) + "  y=" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + str(y)))))))) + "  d=" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + str(d)))))))))
    if not (j or (r or (b or v))):
        if x < 700 and y < 700:
            if x > 300 and y > 300:
                radio.send_value("stop", 0)
                basic.clear_screen()
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    """)
    if x < 200:
        radio.send_value("left", x)
        basic.show_arrow(ArrowNames.WEST)
    if x > 824:
        radio.send_value("right", x)
        basic.show_arrow(ArrowNames.EAST)
    if y < 200:
        radio.send_value("backward", y)
        basic.show_arrow(ArrowNames.SOUTH)
    if y > 824:
        basic.show_arrow(ArrowNames.NORTH)
        radio.send_value("forward", y)
    if r:
        radio.send_value("autodestrcution", 1)
        basic.show_string("R")
    if j:
        radio.send_value("klaxon", 15)
        basic.show_string("J")
    if b:
        radio.send_value("lightright", 1)
        basic.show_string("B")
    if v:
        radio.send_value("V", 1)
        basic.show_string("V")
    if t:
        radio.send_value("klaxon", 1)
    if d > 100:
        radio.send_value("autopilot", 0)
        while d > 100:
            d = bitcommander.read_dial()
            a = randint(0, 5)
            d = bitcommander.read_dial()
            if a == 0:
                d = bitcommander.read_dial()
            if a == 1:
                radio.send_value("forward", randint(824, 1024))
                d = bitcommander.read_dial()
            if a == 2:
                radio.send_value("backward", randint(0, 200))
                d = bitcommander.read_dial()
            if a == 3:
                radio.send_value("left", randint(0, 200))
                d = bitcommander.read_dial()
            if a == 4:
                radio.send_value("right", randint(824, 1024))
                d = bitcommander.read_dial()
            d = bitcommander.read_dial()
            basic.pause(5000)
            d = bitcommander.read_dial()
    else:
        bitcommander.led_clear()