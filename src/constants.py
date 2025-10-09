#!/usr/bin/env python3

import os
from dotenv import load_dotenv

# Load environment variables from .env file in the project root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Constants
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model
GEMINI_MODEL = "gemini-2.5-flash"

# Endpoint
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

# Headers
HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY
}
