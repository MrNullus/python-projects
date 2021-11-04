lista = list()

for c in range(0, 5):
    n = int(input("Digite um número:>> "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}...')
                break
            pos += 1

print('=-===-='*6)
print(f'Valores digitados ordenados : {lista}')
print('=-===-='*6)
