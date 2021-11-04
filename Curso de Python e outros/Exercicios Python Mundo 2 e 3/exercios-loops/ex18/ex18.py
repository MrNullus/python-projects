tot18 = totH = totM20 = 0

while True:
    print("=== CADASTRO PESSOA ===")
    print('---' * 8)
    idade = int(input("Digite a idade:> "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Qual o sexo [F/M]? ")).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'M' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
        print('---' * 8)
    if resp == 'N':
        break
print('=-=-=' * 10)
print(f'    Total de pessoas com mais de 18 anos é {tot18}')
print(f'    Tem um total de {totH} homens')
print(f'    São {totM20} mulheres com menos de 20 anos')
print('=-=-=' * 10)