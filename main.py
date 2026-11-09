from voice.listener import listen
from voice.speaker import speak
from voice.wake_word import wait_for_wake_word
from brain import ask_ai, clear_memory


def main():

    speak("Hello Bhai! Jarvis is ready.")

    while True:

        # Wait for Hey Jarvis
        wait_for_wake_word()

        speak("Yes Bhai, I am listening.")

        # Listen to user's command
        command = listen()

        if not command:
            continue

        # Exit command
        if command in ["exit", "stop jarvis", "shutdown jarvis"]:
            speak("Goodbye Bhai!")
            break

        # Clear conversation memory
        if "clear memory" in command:
            clear_memory()
            speak("Memory cleared.")
            continue

        # Ask Gemini AI
        print("JARVIS: Thinking...")

        response = ask_ai(command)

        speak(response)


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nJARVIS stopped.")