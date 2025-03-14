def func_randomize_world():
    for cell_id in range(25):
        world[cell_id] = randint(0, 1)
def func_init():
    global generation, world, world2, friends_matrix
    generation = 0
    world = [25]
    world2 = [25]
    friends_matrix = [[-1, -1, -6],
        [0, -1, -5],
        [1, -1, -4],
        [-1, 0, -1],
        [1, 0, 1],
        [-1, 1, 4],
        [0, 1, 5],
        [1, 1, 6]]
def func_render():
    basic.clear_screen()
    for cell_id2 in range(25):
        if world[cell_id2]:
            led.plot(cell_id2 - 5 * abs(Math.idiv(cell_id2, 5)),
                abs(Math.idiv(cell_id2, 5)))
def func_next_generation():
    global friends, target_cell_x, target_cell_y, target_cell_id, new_cell, generation
    for cell_id3 in range(25):
        friends = 0
        for offset in friends_matrix:
            target_cell_x = cell_id3 - 5 * abs(Math.idiv(cell_id3, 5)) + offset[0]
            target_cell_y = abs(Math.idiv(cell_id3, 5)) + offset[1]
            target_cell_id = cell_id3 + offset[2]
            if target_cell_x >= 0 and target_cell_x < 5 and (target_cell_y >= 0 and target_cell_y < 5):
                if world[target_cell_id]:
                    friends += 1
        new_cell = 0
        if world[cell_id3]:
            if friends < 2 or friends > 3:
                new_cell = 0
            else:
                new_cell = 1
        else:
            if friends == 3:
                new_cell = 1
        world2[cell_id3] = new_cell
    generation += 1

def on_button_pressed_a():
    func_randomize_world()
    func_render()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(generation)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    func_next_generation()
    func_swap_worlds()
    func_render()
input.on_button_pressed(Button.B, on_button_pressed_b)

def func_swap_worlds():
    for cell_id4 in range(25):
        world[cell_id4] = world2[cell_id4]
new_cell = 0
target_cell_id = 0
target_cell_y = 0
target_cell_x = 0
friends = 0
friends_matrix: List[List[number]] = []
world2: List[number] = []
generation = 0
world: List[number] = []
func_init()
func_randomize_world()
func_render()

def on_forever():
    func_next_generation()
    func_swap_worlds()
    func_render()
    basic.pause(1000)
basic.forever(on_forever)