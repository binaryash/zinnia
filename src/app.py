#!/usr/bin/env python3


from genai import gemini_handler

def main():
    response = gemini_handler.run_prompt("Hello from app.py!")
    print(response)

if __name__ == "__main__":
    main()
