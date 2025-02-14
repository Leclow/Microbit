radio.set_group(32)

def on_button_pressed_a():
    radio.send_string("forward")
    radio.send_number(50)

input.on_button_pressed(Button.A, on_button_pressed_a)

#new main
radio.set_group(32)

def on_button_pressed_a():
    radio.send_string("FORWARD")
    radio.send_number(50)

input.on_button_pressed(Button.A, on_button_pressed_a)


#
radio.set_group(32)

def on_button_pressed_a():
    radio.send_string("left")

def on_button_pressed_b():
    radio.send_string("right")


input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)