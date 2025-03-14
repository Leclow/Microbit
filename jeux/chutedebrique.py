def on_button_pressed_a():
    global posX, posY
    if verif == 0:
        led.unplot(posX, posY)
        posX += -1
        if posX < 0:
            posX += 1
        posY += 0
        led.plot(posX, posY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global posX, posY
    if verif == 0:
        led.unplot(posX, posY)
        posX += 1
        if posX > 4:
            posX += -1
        posY += 0
        led.plot(posX, posY)
input.on_button_pressed(Button.B, on_button_pressed_b)

EnposY1 = 0
EnposX1 = 0
EnpoxY = 0
EnposX = 0
posY = 0
posX = 0
lancement1 = 0
lancement = 0
verif = 0
verif = 0
if verif == 0:
    lancement = 0
    lancement1 = 0
    lancement += 1
    posX = 2
    posY = 4
    led.plot(posX, posY)

def on_forever():
    global verif
    if posX == EnposX and posY == EnpoxY:
        verif = 1
        basic.clear_screen()
        for index in range(4):
            basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . # . # .
                """)
            basic.pause(100)
            basic.show_leds("""
                . . # . .
                . # # . .
                # # . # #
                . # . . .
                . # # . .
                """)
            basic.pause(100)
basic.forever(on_forever)

def on_forever2():
    global lancement, EnposX, EnpoxY
    if verif == 0:
        if lancement == 1 or lancement == 3:
            if lancement == 1:
                lancement += 2
                EnposX = randint(0, 5)
                EnpoxY = 0
                for index2 in range(5):
                    led.plot(EnposX, EnpoxY)
                    basic.pause(100)
                    led.unplot(EnposX, EnpoxY)
                    EnpoxY += 1
                    led.plot(EnposX, EnpoxY)
                lancement = 1
basic.forever(on_forever2)

def on_forever3():
    global lancement1, EnposX1, EnposY1, EnpoxY
    basic.pause(200)
    if verif == 0:
        if lancement1 == 1 or lancement1 == 3:
            if lancement1 == 1:
                lancement1 += 2
                EnposX1 = randint(0, 5)
                EnposY1 = 0
                for index3 in range(5):
                    led.plot(EnposX1, EnposY1)
                    basic.pause(100)
                    led.unplot(EnposX1, EnposY1)
                    EnpoxY += 1
                    led.plot(EnposX1, EnposY1)
                lancement1 = 1
basic.forever(on_forever3)