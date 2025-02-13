import requests
import json

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/v1/chat/completions"

def chat_with_groq():
    print("Chat with Groq! Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": user_input}]
        }

        try:
            response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(data))
            response_json = response.json()

            # Extract and display the response from Groq
            if "choices" in response_json and response_json["choices"]:
                bot_reply = response_json["choices"][0]["message"]["content"]
                print("\nGroq:", bot_reply)
            else:
                print("\nGroq: (No response received)")

        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    chat_with_groq()
