valores = list()
lista_par = []; lista_impar = []


while True:
    valores.append(int(input("$ Digite um valor:>> ")))

    resp = str(input('$ Quer continuar? <S/N>'))
    if resp in 'Nn':
        break

    for v in valores:
        if v % 2 == 0:
            lista_par.append(v)
        else:
            lista_impar.append(v)

print(f'@ Lista Completa : {valores}')
print(f'@ Lista dos valores pares : {lista_par}')
print(f'@ Lista dos valores impares : {lista_impar}')