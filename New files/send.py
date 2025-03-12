def on_button_pressed_a():
    radio.send_value("lightleft", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("lightright", 1)
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
    print("x=" + ("" + ("" + ("" + str(x)))) + "  y=" + ("" + ("" + ("" + str(y)))) + "  d=" + ("" + ("" + ("" + str(d)))))
    if x < 700 and y < 700:
        if x > 300 and y > 300:
            basic.clear_screen()
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
            radio.send_value("stop", 1)
    if x < 200:
        basic.show_arrow(ArrowNames.WEST)
        radio.send_value("left", x)
    if x > 824:
        basic.show_arrow(ArrowNames.EAST)
        radio.send_value("right", x)
    if y < 200:
        basic.show_arrow(ArrowNames.SOUTH)
        radio.send_value("backward", y)
    if y > 824:
        basic.show_arrow(ArrowNames.NORTH)
        radio.send_value("forward", y)
    if d > 10:
        bitcommander.set_led_color(Math.idiv(d, 3))
        bitcommander.led_show()
    else:
        bitcommander.led_clear()
    if r:
        basic.show_string("R")
        radio.send_value("klaxon", 1)
    if j:
        basic.show_string("J")
        radio.send_string("J")
    if b:
        basic.show_string("B")
        radio.send_string("B")
    if v:
        basic.show_string("V")
        radio.send_string("V")
    