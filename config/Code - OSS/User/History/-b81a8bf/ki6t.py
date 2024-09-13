import request
print(request.get('https://api.dictionaryapi.dev/api/v2/entries/en/hello').status())