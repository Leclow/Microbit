"""

Sets the speed of the moving LED and has a 1 second pause before the LED falls

"""
# Checks if the game is over (a column is full at the top row). If the column is full, then GAME OVER!!!!
def checkGameOver():
    for col5 in range(5):
        if led.point(col5, 0):
            gameOver()
            return
# When the A button is pressed, move the LED left by one position.

def on_button_pressed_a():
    global x
    if x > 0 and not (led.point(x - 1, y)):
        # Check if the left position is empty
        led.unplot(x, y)
        x += 0 - 1
        led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

# This function handles the row clearing for when a row is full. If it is full, the row flashes and you gain 1 score.
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
# This function flashes a row before clearing it.
def flashRow(row2: number):
    for index in range(3):
        for col3 in range(5):
            led.plot(col3, row2)
        basic.pause(100)
        for col4 in range(5):
            led.unplot(col4, row2)
        basic.pause(100)
# Displays a game-over screen and stops the game with also showing what your score was.
def gameOver():
    basic.clear_screen()
    basic.show_string("GAME OVER SCORE")
    basic.show_string("" + str(score))
    # Restart the game after displaying "GAME OVER".
    control.reset()
# When the B button is pressed, move the LED right by one position.

def on_button_pressed_b():
    global x
    if x < 4 and not (led.point(x + 1, y)):
        # Check if the right position is empty
        led.unplot(x, y)
        x += 1
        led.plot(x, y)
input.on_button_pressed(Button.B, on_button_pressed_b)

score = 0
fullRow = False
y = 0
x = 0
x = 2
speed = 500
basic.clear_screen()
basic.pause(1000)
# Handles the LED falling down the grid.

def on_forever():
    global y, x
    led.plot(x, y)
    basic.pause(speed)
    # If the falling LED is not at the bottom and the space below it is empty, move it down.
    # If the falling LED reaches the floor or encounters another LED, stop the fall.
    # Reset x to the middle position after falling
    if y < 4 and not (led.point(x, y + 1)):
        led.unplot(x, y)
        y += 1
    else:
        clearFullRows()
        y = 0
        x = 2
    # Prevent the falling LED from moving past another LED to the left or right when on the floor.
    if y == 4:
        # Prevent movement past LED on left
        if x > 0 and led.point(x - 1, y):
            x = x
        # Prevent movement past LED on right
        if x < 4 and led.point(x + 1, y):
            x = x
basic.forever(on_forever)

# Plays the Tetris theme song forever.

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