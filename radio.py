while True:
    message = radio.receive()
    if message:
        if message == 'klax':
            display.show(Image.HEART)
        elif message != 'klax':
            display.show(Image.BUTTERFLY)