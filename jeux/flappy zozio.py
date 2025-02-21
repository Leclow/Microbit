def on_button_pressed_a():
    zozio.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    zozio.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.B, on_button_pressed_b)

emptyObstacleY = 0
hole_size = 1
ticks = 0
zozio: game.LedSprite = None
index = 0
obstacles: List[game.LedSprite] = []
zozio = game.create_sprite(0, 2)
zozio.set(LedSpriteProperty.BLINK, 300)

def on_forever():
    zozio.change(LedSpriteProperty.Y, 1)
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    global emptyObstacleY, hole_size, ticks

    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
 
    for obstacle2 in obstacles:
        obstacle2.change(LedSpriteProperty.X, -1)
    
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 3) 
        hole_size = randint(1, 2) 

        for index2 in range(5):
            if not (emptyObstacleY <= index2 < emptyObstacleY + hole_size):
                obstacles.append(game.create_sprite(4, index2))


    for obstacle3 in obstacles:
        if obstacle3.get(LedSpriteProperty.X) == zozio.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == zozio.get(LedSpriteProperty.Y):
            game.game_over()

    ticks += 1
    basic.pause(1000)

basic.forever(on_forever2)
