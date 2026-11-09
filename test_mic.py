from voice.listener import listen

while True:
    command = listen()

    if command:
        print("Recognized:", command)
        break