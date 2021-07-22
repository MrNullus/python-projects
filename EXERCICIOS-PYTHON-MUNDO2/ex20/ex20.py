print('=' * 30)
print('{:^30}'.format(' BANCO DO GUSTAFE '))
print('=' * 30)

valor = int(input("- Que valor você quer retirar? R$ "))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'#   Um total de {totced} céculas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break


print('{:-^40}'.format(' FIM DO PROGRAMA '))
print("Obrigado por usar o Banco GUSTAFE. Volte sempre!")
print('='*30)