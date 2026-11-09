from brain import ask_ai

while True:
    question = input("\nYOU: ")

    if question.lower() == "exit":
        print("JARVIS: Goodbye!")
        break

    answer = ask_ai(question)
    print("\nJARVIS:", answer)