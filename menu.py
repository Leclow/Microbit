from jeux.MERGE import bataillenavale, chutedebrique, chutedevoiture, spaceinvader


def menu():
    Mod = 0
    allMods = ["car",
           "badapple",
           "bataillenavale",
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
        if not (j or (r or (b or v))):
            #To know the selected Mod
            basic.clear_screen()
            basic.show_string(Mod)
        if r:
            Mod = 0
            basic.show_string(Mod)
            # reset to car mod
        if j:
            if Mod > 0:
                Mod -= 1
            else:
                Mod = len(allMods)-1
            basic.show_string(Mod)
            # minus 1
        if b:
            if Mod < len(allMods)-1:
                Mod += 1
            else:
                Mod = 0
            # add 1
            basic.show_string(Mod)
        if v:
            # launch the game
            if Mod == 0:
                CarMod()
            elif Mod == 1:
                badapple()
            elif Mod == 2:
                bataillenavale()
            elif Mod == 3:
                chutedebrique()
            elif Mod == 4:
                chutedevoiture()
            elif Mod == 5:
                floppybird()
            elif Mod == 6:
                gameoflife()
            elif Mod == 7:
                pongsolo()
            elif Mod == 8:
                spaceinvader()
            elif Mod == 9:
                tetris()
        else:
            bitcommander.led_clear()


def CarMod():
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
        #print("x=" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + str(x))))))))))))) + "  y=" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + str(y))))))))))))) + "  d=" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + ("" + str(d))))))))))))))
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
        if r:
            radio.send_value("trump", 1)
            basic.show_string("R")
        if j:
            radio.send_value("ll", 15)
            basic.show_string("J")
        if b:
            radio.send_value("lr", 1)
            basic.show_string("B")
        if v:
            radio.send_value("V", 1)
            basic.show_string("V")
        if t:
            radio.send_value("k", 1)
        if d > 100:
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