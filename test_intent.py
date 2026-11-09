from intelligence.intent_detector import detect_intent

tests = [
    "Search Python roadmap on YouTube",
    "Open Chrome",
    "Close Notepad",
    "What is Machine Learning?"
]

for command in tests:
    print(command, "→", detect_intent(command))