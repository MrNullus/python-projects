def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('\033[0;31m ERRO! Digite apenas números inteiros validos!. \033[m')
        if ok:
            break
    return valor

n = leiaInt('$ Digite um número:  ')
print(f'+=> Você digitou o número {n}')