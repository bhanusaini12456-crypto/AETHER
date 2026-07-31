import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def ask_gemini(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(URL, headers=headers, data=json.dumps(data), timeout=60)

    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]

    return f"Error {response.status_code}: {response.text}"


if __name__ == "__main__":
    while True:
        prompt = input("Bhanu > ")

        if prompt.lower() == "exit":
            break

        print("\nAETHER >")
        print(ask_gemini(prompt))
        print()
