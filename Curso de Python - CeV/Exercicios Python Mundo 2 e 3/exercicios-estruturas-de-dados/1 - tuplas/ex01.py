cont = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezesete', 'dezoito',
    'dezenove', 'vinte'
)
while True:
    num = int(input("Digite um número, entre 0 e 20:> "))
    print(f'O número digitado é {cont[num]}')

    if 0 <= num <= 20:
        break

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == 'N':
        break