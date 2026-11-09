from automation.command_handler import handle_command

commands = [
    "open chrome",
    "open notepad",
    "open calculator",
    "close notepad"
]

for command in commands:

    print("\nYOU:", command)

    response = handle_command(command)

    print("JARVIS:", response)