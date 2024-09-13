import requests

response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/run')
data = response.json()  # Convert the response to JSON format

meanings = data[0]['meanings']
print("\nMeanings:")
for meaning in meanings:
    print(meaning['partOfSpeech'])
    print(meaning['definitions'][0]['definition'])
    print("="*50 + "\n")
