def on_forever():
    if autopilot:
        possible_actions = ["stop", "forward", "backward", "left", "right"]
        action = possible_actions[randint(0, 5)]
        speed = randint(0, 100)
        radio.send_value(action, speed)
basic.forever(on_forever)
