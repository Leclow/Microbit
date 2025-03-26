
def menu():
    Mod = 0
    allMods = ["car",
           "badapple",
           "chutev",
           "chute",
           "floppy bird",
           "game_of_life",
           "pong",
           "invaders",
           "tetris"]
    while True:
        r = bitcommander.read_button(BCButtons.RED)
        j = bitcommander.read_button(BCButtons.YELLOW)
        b = bitcommander.read_button(BCButtons.BLUE)
        v = bitcommander.read_button(BCButtons.GREEN)
        if not (j or (r or b)):
            #To know the selected Mod
            basic.clear_screen()
            basic.show_number(Mod)
        if v:
            Mod = 0
            # reset to car mod
        if j:
            if Mod > 0:
                Mod -= 1
            else:
                Mod = len(allMods)-1
            basic.show_number(Mod)
            # minus 1
        if b:
            if Mod < len(allMods)-1:
                Mod += 1
            else:
                Mod = 0
            # add 1
            basic.show_number(Mod)
        if r:
            # launch the game
            if Mod == 0:
                CarMod()
        else:
            bitcommander.led_clear()


def CarMod():
    while True:
        x = bitcommander.read_joystick(BCJoystick.X)
        y = bitcommander.read_joystick(BCJoystick.Y)
        d = bitcommander.read_dial()
        t = bitcommander.read_button(BCButtons.JOYSTICK)
        r = bitcommander.read_button(BCButtons.RED)
        j = bitcommander.read_button(BCButtons.YELLOW)
        b = bitcommander.read_button(BCButtons.BLUE)
        v = bitcommander.read_button(BCButtons.GREEN)
        if not (j or (r or (b or v))):
            if x < 700 and y < 700:
                if x > 300 and y > 300:
                    radio.send_value("s", 0)
                    basic.clear_screen()
                    basic.show_leds("""
                        . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
                        """)
        if x < 200:
            radio.send_value("l", x)
            basic.show_arrow(ArrowNames.WEST)
        if x > 824:
            radio.send_value("r", x)
            basic.show_arrow(ArrowNames.EAST)
        if y < 200:
            radio.send_value("b", y)
            basic.show_arrow(ArrowNames.SOUTH)
        if y > 824:
            basic.show_arrow(ArrowNames.NORTH)
            radio.send_value("f", y)
        if v:
            radio.send_value("s", 1)
            menu()
        if r:
            radio.send_value("trump", 1)
            basic.show_string("R")
        if j:
            radio.send_value("ll", 15)
            basic.show_string("J")
        if b:
            radio.send_value("lr", 1)
            basic.show_string("B")
        if bitcommander.read_button(BCButtons.GREEN):
            menu()
        if t:
            radio.send_value("k", 1)
        if d > 100 :
            radio.send_value("autopilot", 0)
            while d > 100:
                d = bitcommander.read_dial()
                a = randint(0, 5)
                d = bitcommander.read_dial()
                if a == 0:
                    d = bitcommander.read_dial()
                if a == 1:
                    radio.send_value("f", randint(824, 1024))
                    d = bitcommander.read_dial()
                if a == 2:
                    radio.send_value("b", randint(0, 200))
                    d = bitcommander.read_dial()
                if a == 3:
                    radio.send_value("l", randint(0, 200))
                    d = bitcommander.read_dial()
                if a == 4:
                    radio.send_value("r", randint(824, 1024))
                    d = bitcommander.read_dial()
                d = bitcommander.read_dial()
                basic.pause(5000)
                d = bitcommander.read_dial()
        else:
            bitcommander.led_clear()
radio.set_group(44)
menu()