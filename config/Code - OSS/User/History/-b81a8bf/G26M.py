import  freedictionaryapi as p
with open('file.txt','w')as d:
    d.write(help(p))
# with freedictionaryapi() as client:
#     inp = input()
#     response = client.get_definition(inp)
#     print(reponse['status'])
