temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:]) # Para copiar uma lista ou inserir uma na outra precisa-se usar assim: lista(:) sem os dois pontos não copia
    temp.clear()

    resp = str(input('Você quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print("+-++-+"*10)
print(f'- Os dados foram {princ}')
print(f'- Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'- O maior pesso foi de {mai}Kg. Peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f' {p[0]}')
print(f'- O menor peso foi de {men}Kg. Peso de', end='')
for p in princ:
    if p[1] == men:
        print(f' {p[0]}', end='')
print("\n+-++-+"*10)
