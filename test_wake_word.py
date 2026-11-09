from voice.wake_word import wait_for_wake_word

print("Say: Hey Jarvis")

result = wait_for_wake_word()

if result:
    print("SUCCESS: JARVIS ACTIVATED!")