import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env into the environment
load_dotenv()

# Read the API key from environment (never hardcode it)
api_key = os.getenv("GEMINI_API_KEY")

# Create a client — this is your gateway to Gemini
client = genai.Client(api_key=api_key)

# Make your first call
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello and confirm you're working, in one sentence."
)

print(response.text)