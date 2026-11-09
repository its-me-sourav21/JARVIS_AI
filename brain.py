import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"

conversation = []
SYSTEM_INSTRUCTION = """
You are JARVIS, a personal voice assistant.

You have voice output through a Python text-to-speech system.

IMPORTANT:
- Never claim that you are text-only.
- Never tell the user to install browser extensions for voice.
- You can respond through your connected voice system.
- Understand Hindi, English and Hinglish.
- Keep answers short and conversational.
- You are the user's personal AI assistant.
"""

def ask_ai(user_input):

    if not user_input.strip():
        return "Bhai, kuch bolo!"

    conversation.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=conversation,
            config={
                "system_instruction": SYSTEM_INSTRUCTION,
                "temperature": 0.5,
                "max_output_tokens": 250
            }
        )

        answer = response.text

        if not answer:
            answer = "I couldn't generate a response."

        conversation.append({
            "role": "model",
            "parts": [{"text": answer}]
        })

        return answer

    except Exception as e:

        conversation.pop()

        print("AI ERROR:", e)

        return "Sorry Bhai, AI service is temporarily unavailable."


def clear_memory():
    conversation.clear()
    return "Memory cleared!"