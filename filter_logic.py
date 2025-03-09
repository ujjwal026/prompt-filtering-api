import os
from google import genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

def process_prompt(prompt):
    """Determine if the prompt is safe, and generate a response accordingly."""
    moderation_prompt = f"""
    Analyze the following user query and determine if it should be BLOCKED or ALLOWED.
    Respond with ONLY "BLOCK" (if it should be blocked) or "ALLOW" (if it is safe).
    
    Query: "{prompt}"
    """

    try:
        # Check if prompt is safe
        mod_response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=moderation_prompt
        ).text.strip()

        print(f"🔍 Moderation Response: {mod_response}")

        if mod_response.upper() == "BLOCK":
            return "❌ This request is blocked due to security concerns."
        
        # If allowed, generate a real response
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text.strip()  # Return AI's actual response

    except Exception as e:
        print(f"⚠️ Error checking prompt safety: {e}")
        return "⚠️ Unable to process request at this time."
