from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0

print("---======---- PALPITEIRO MEGA SENA ---======---")

quant = int(input('Digite quantos jogos quer que eu sortei:>> '))
tot = 1

print("-----------  SORTEANDO  ------------")
sleep(2)
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)

print("-----------  BOA SORTE  ------------")
print("----======-----======-----======-----======")