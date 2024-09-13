import requests
response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/run')
for i in response:
    print(i)