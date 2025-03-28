def tetris():
    def checkGameOver():
        for col5 in range(5):
            if led.point(col5, 0):
                gameOver()
                return


    def on_button_pressed_a():
        global x23
        if x23 > 0 and not (led.point(x23 - 1, y)):
            
            led.unplot(x23, y23)
            x23 += 0 - 1
            led.plot(x23, y23)
    input.on_button_pressed(Button.A, on_button_pressed_a)

    def clearFullRows():
        global fullRow, score
        for row in range(5):
            fullRow = True
            for col in range(5):
                if not (led.point(col, row)):
                    fullRow = False
                    break
            if fullRow:
                flashRow(row)
                for col2 in range(5):
                    led.unplot(col2, row)
                score += 1
                r = row
                while r > 0:
                    for c in range(5):
                        if led.point(c, r - 1):
                            led.plot(c, r)
                        else:
                            led.unplot(c, r)
                    r += 0 - 1
        checkGameOver()

    def flashRow(row2: number):
        for index in range(3):
            for col3 in range(5):
                led.plot(col3, row2)
            basic.pause(100)
            for col4 in range(5):
                led.unplot(col4, row2)
            basic.pause(100)
    def gameOver():
        basic.clear_screen()
        basic.show_string("GAME OVER SCORE")
        basic.show_string("" + str(score))
        control.reset()

    def on_button_pressed_b():
        global x23
        if x23 < 4 and not (led.point(x23 + 1, y23)):
            led.unplot(x23, y23)
            x23 += 1
            led.plot(x, y23)
    input.on_button_pressed(Button.B, on_button_pressed_b)

    score = 0
    fullRow = False
    y23 = 0
    x23 = 0
    x23 = 2
    speed = 500
    basic.clear_screen()
    basic.pause(1000)

    def on_forever():
        global y23, x23
        led.plot(x23, y23)
        basic.pause(speed)
    
        if y23 < 4 and not (led.point(x23, y23 + 1)):
            led.unplot(x23, y23)
            y23 += 1
        else:
            clearFullRows()
            y23 = 0
            x23 = 2
        if y23 == 4:

            if x23 > 0 and led.point(x23 - 1, y23):
                x23 = x23
            if x23 < 4 and led.point(x23 + 1, y23):
                x23 = x23
    basic.forever(on_forever)


    def on_forever2():
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        basic.pause(400)
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.HALF))
        music.play_tone(440, music.beat(BeatFraction.HALF))
        music.play_tone(440, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.play_tone(349, music.beat(BeatFraction.HALF))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.HALF))
    basic.forever(on_forever2)