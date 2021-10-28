from random import randint
from time import sleep

def sorteia(lista):
    print('-= Sorteaando valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Prontinho!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'-= Somando os valores pares de {lista} tem {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)
