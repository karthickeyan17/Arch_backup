import requests
response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/hello')
print(response.__dict__)