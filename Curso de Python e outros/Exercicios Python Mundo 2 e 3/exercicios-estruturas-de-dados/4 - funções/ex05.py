from time import sleep

def maior(* num):
    print('=-='*14)
    print('Analizando valores passados......')
    cont = maior = 0
    for valor in num:
        print(f'{valor}; ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('=-=' * 14)


maior(2, 6, 10, 1)
maior(12, 6, 9, 90)