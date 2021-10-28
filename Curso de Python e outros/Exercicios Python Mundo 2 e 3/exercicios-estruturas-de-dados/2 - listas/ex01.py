# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
listaNum = []
maior = 0
menor = 0

print(f'{" ":=^50}')
for c in range(6):
    listaNum.append(int(input(f'Digite o valor na posição {c}:>> ')))
    if c == 0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c] > maior:
            maior = listaNum[c]
        elif listaNum[c] < menor:
            menor = listaNum[c]

print(f'{" ":=^50}')
print(f'- Valores da lista: {listaNum}')
print(f'-= O maior valor é := {maior} nas posições := ', end='')
for i, v in enumerate(listaNum):
    if v == maior:
        print(i, end='...')
print()

print(f'-= O menor valor é := {menor} nas posições := ', end='')
for i, v in enumerate(listaNum):
    if v == menor:
        print(i, end=' ')
print()
print(f'{" ":=^50}')
