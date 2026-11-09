from automation.command_handler import handle_command
from voice.listener import listen
from voice.speaker import speak
from voice.wake_word import wait_for_wake_word
from brain import ask_ai, clear_memory


def conversation_mode():

    speak("Yes Bhai, I am listening.")

    while True:

        command = listen()

        if not command:
            continue

        # Exit conversation mode
        if any(word in command for word in [
            "goodbye jarvis",
            "sleep jarvis",
            "go to sleep",
            "stop listening"
        ]):
            speak("Okay Bhai. Going to sleep.")
            return

        # Clear conversation memory
        if "clear memory" in command:
            clear_memory()
            speak("Conversation memory cleared.")
            continue

        # Shutdown assistant
        if any(word in command for word in [
            "shutdown jarvis",
            "exit jarvis",
            "quit jarvis"
        ]):
            speak("Goodbye Bhai. Shutting down.")
            raise SystemExit

       # Check system commands first
        response = handle_command(command)

        if response:
            speak(response)
            continue

        # Otherwise use Gemini AI
        print("JARVIS: Thinking...")

        response = ask_ai(command)

        speak(response)


def main():

    speak("Hello Bhai. All systems are ready.")

    while True:

        print("\nJARVIS: Sleeping. Say Hey Jarvis to activate.")

        wait_for_wake_word()

        conversation_mode()


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nJARVIS stopped.")
 