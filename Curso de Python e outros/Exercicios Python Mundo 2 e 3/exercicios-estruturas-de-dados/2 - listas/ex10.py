matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'$ Digite o valor para [{l},{c}]:>> '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

for l in range(0, 3):
    for c in range(0,3):
        print(f' [ {matriz[l][c]:^5} ]', end='')
    print()

print('-=-=-' * 10)
print(f'A soma dos valores pares é: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):
    if matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior número é: {mai}')