import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("JARVIS: Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        command = recognizer.recognize_google(audio)

        print("YOU:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        print("JARVIS: No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("JARVIS: Could not understand.")
        return ""

    except sr.RequestError:
        print("JARVIS: Speech service unavailable.")
        return ""

    except Exception as e:
        print("MIC ERROR:", e)
        return ""