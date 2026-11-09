import pyttsx3

print("Initializing voice engine...")

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
print("Available voices:")

for voice in voices:
    print(voice.id, voice.name)

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

print("Speaking test...")
engine.say("Hello Bhai, I am Jarvis. Can you hear me?")
engine.runAndWait()

print("Test completed.")