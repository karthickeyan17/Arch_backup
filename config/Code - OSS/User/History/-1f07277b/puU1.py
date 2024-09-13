import requests
import json

# Define your API key
API_KEY = 'your_api_key'

# Define the endpoint URL
url = "https://translation.googleapis.com/language/translate/v2"

# Define the request parameters
params = {
    'q': 'Hello, world!',  # Text to be translated
    'target': 'es',        # Target language (Spanish)
    'source': 'en',        # Source language (English)
    'format': 'text',      # Format of the source text
    'key': API_KEY         # API key
}

# Make the POST request
response = requests.post(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Print the translated text
    translated_text = data['data']['translations'][0]['translatedText']
    print(f"Translated text: {translated_text}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
