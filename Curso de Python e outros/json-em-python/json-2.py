import json

# Usar um arquivo JSON externo
# Se  for trabalhar com arquivo externo use load()
with open('/json-em-python/jogador.json') as file:
    jogador = json.load(file)

def linha():
    print("-" * 26)

linha()
#chaves
for keys in jogador:
    print(keys)
print("----" * 5)
linha()

#itens
for items in jogador.items():
    print(items)
print("----" * 5)
linha()

#valores
for values in jogador.values():
    print(values)
print("----" * 5)
linha()

#nome do jogador
print(jogador["nome"])
print("----" * 5)
linha()

#time jogador
print(jogador["time"])
linha()

#itens da mochila
for itemsMochila in jogador["mochila"]:
    print(itemsMochila)
linha()

#Aeronaves
print("-" * 26)
print("     Aeronaves    ")
for aeronave in jogador["aeronaves"]:
    print("-" * 26)
    print(f'Nome       - {aeronave["nome"]:>6}')
    print(f'Tipo       - {aeronave["tipo"]:>6}')
    print(f'Habilidade - {aeronave["habilidade"]:>6}')
    print("-" * 26)
linha()
