import openai
import json

# Load API key from config
with open('core/config.json', 'r') as f:
    config = json.load(f)

openai.api_key = config["openai_api_key"]

def get_ai_response(prompt):
    """ Sends a query to OpenAI and returns the response. """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Change model if needed
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"
