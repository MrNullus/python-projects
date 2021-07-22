s = 0
cont = 0
for c in range(0,6):
    num = int(input(f'Digite o {c} : '))
    if num % 2 == 0:
        s += num
        cont += 1

print("O numero de PARES são: {} \nA soma dos pares são: {}".format(cont, s))