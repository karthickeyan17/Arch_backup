import requests
response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/run')
for definition in response.content:
    print(definition)