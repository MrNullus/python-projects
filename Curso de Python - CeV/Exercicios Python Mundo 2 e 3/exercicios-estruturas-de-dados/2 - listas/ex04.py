lista_num = []

while True:
    lista_num.append(int(input("Digite um numero:>> ")))

    resp = str(input("Quer continuar? [S/N] ").strip().upper())
    if resp in 'Nn':
        break

print("++---++"*9)
print(f'# A lista tem um total de {len(lista_num)} elementos')
lista_num.sort(reverse=True)
print(f'# Os valores em ordem decrescente são : {lista_num}')
if 5 in lista_num:
    print('# O número 5 está na lista')
else:
    print('# O número 5 não está na lista')
print("++---++"*9)