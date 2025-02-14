import requests
import json

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat_with_groq():
    print("Welcome to Groq Chat! Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("Exiting chat. Have a great day!")
            break

        response = get_groq_response(user_input)
        print("\nGroq:", response if response else "(No response received)")

def get_groq_response(user_input):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response_json = response.json()

        if response.status_code == 200 and "choices" in response_json:
            return response_json["choices"][0]["message"]["content"]
        return None

    except requests.exceptions.RequestException:
        return None

if __name__ == "__main__":
    chat_with_groq()
