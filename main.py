from voice.listener import listen
from voice.speaker import speak
from brain import ask_ai, clear_memory


def main():

    speak("Hello! I am Jarvis. All systems are ready.")

    while True:

        command = listen()

        if not command:
            continue

        if command in ["exit", "stop jarvis", "shutdown jarvis"]:
            speak("Goodbye Bhai!")
            break

        if "clear memory" in command:
            clear_memory()
            speak("Memory cleared.")
            continue

        print("JARVIS: Thinking...")

        response = ask_ai(command)

        speak(response)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nJARVIS stopped.")