num = 0; cont = 0; soma = 0
num = int(input("Digite um numero [999 para parar]:>   "))

while num != 999: #999 é um flag, flags são paradas
    num = int(input("Digite um numero [999 para parar]:>   "))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma dos {cont} numeros é {soma}')