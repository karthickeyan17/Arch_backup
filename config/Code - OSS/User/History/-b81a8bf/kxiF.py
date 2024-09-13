from freeDictionaryAPI import FreeDictionaryAPI
with FreeDictionaryApi() as client:
    inp = input()
    response = client.get_definition(inp)
    print(reponse['status'])
