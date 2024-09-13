import requests
print(requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/hello').raise_for_status)