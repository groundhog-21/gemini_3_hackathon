import os
from dotenv import load_dotenv

# 1. Load the variables from .env into the system environment
load_dotenv()

# 2. Retrieve the key
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("✅ Success! API Key loaded.")
    # Show only the first 4 characters for safety
    print(f"Key starts with: {api_key[:4]}...")
else:
    print("❌ Error: Could not find GEMINI_API_KEY in .env file.")