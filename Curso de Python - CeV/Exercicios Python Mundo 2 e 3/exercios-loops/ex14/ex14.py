num = 0; cont = 0; soma = 0
num = int(input("Digite um numero [999 para parar]:>   "))

while num != 999: #999 é um flag, flags são paradas
    soma += num
    cont += 1
    num = int(input("Digite um numero [999 para parar]:>   "))

print(f'A soma dos {cont} numeros é {soma}')