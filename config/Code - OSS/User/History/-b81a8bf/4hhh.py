from freedictionaryapi import freedictionaryapi
with freedictionaryapi() as client:
    inp = input()
    response = client.get_definition(inp)
    print(reponse['status'])
