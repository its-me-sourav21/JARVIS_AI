import pyttsx3

def speak(text):
    if not text:
        return

    print("JARVIS:", text)

    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)

    try:
        engine.say(text)
        engine.runAndWait()
    finally:
        engine.stop()
        del engine