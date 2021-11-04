#RegEx
import re

# Expressões regulares servem muito para fazer buscas em strings ou validar strings

text = "Hello World Fi da Égua !!"

# findall() faz a busca e retorna a coleção
# findall(<valor a ser buscado>, <string a ser pesquisada>)
res = re.findall("World", text)

pesq = input("Pesquisar >>  ")
res = re.findall(pesq, text)

print(res)

qtde = len(res)

print(f'Quantidade -> {qtde}')

for t in res:
    print(t)

res = re.search(pesq, text)

if res != None:
    pi = res.start()
    pf = res.end()
    tam = pf - pi
    # Pega o index da primeira ocorrencia
    print(res.start())
    # Pega o index da ultima ocorrencia
    print(res.end())
else:
    print(res)

# Vai cortar a string assim que achar o espaço e colocar o resto em uma list
res = re.split(" ", text)
print(res)
print(res[2])
for t in res:
    print(t)

# Vai trocar um certo valor por outro na string
res = re.sub("!!!",".", text)
# \s -> substitui o espaço
res = re.sub("\s",".", text)
print(res)
