num_princ = [[], []]

for c in range(0, 7):
     num = int(input('Digite a porra de um valor:>> '))
     if num % 2 == 0:
         num_princ[0].append(num)
     else:
         num_princ[1].append(num)

print("===="*9)
print(f'Lista do caralho - ', end='')
num_princ.sort()
for n in num_princ:
    print(f' {n} ', end='')
num_princ[0].sort()
num_princ[1].sort()
print(f'\nLista par   : {num_princ[0]}')
print(f'Lista impar : {num_princ[1]}')
print("===="*9)
