import requests

response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/run')
data = response.json()  # Convert the response to JSON format

# Now you can extract and print specific information from the JSON
for entry in data:
    meanings = entry['meanings']
    print("\nMeanings:")
    for meaning in meanings:
        print(meaning)
        

    
    print("\n" + "="*50 + "\n")
