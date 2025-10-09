#!/usr/bin/env python3
import constants
import requests
import json

GEMINI_API_URL = constants.GEMINI_API_URL
HEADERS = constants.HEADERS

class GeminiTextClient:
    def __init__(self):
        self.endpoint = GEMINI_API_URL
        self.headers = HEADERS

        if not self.headers.get("x-goog-api-key"):
            raise ValueError("Missing Gemini API key. Please set GEMINI_API_KEY in your .env file.")

    def generate_text(self, prompt: str) -> str:
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(
            self.endpoint,
            headers=self.headers,
            data=json.dumps(payload)
        )

        if response.status_code != 200:
            raise Exception(f"Request failed: {response.status_code} - {response.text}")

        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            raise Exception("Unexpected response format", data)

# Add this function:
def run_prompt(prompt: str) -> str:
    client = GeminiTextClient()
    return client.generate_text(prompt)
