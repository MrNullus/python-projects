def fatorial(n, show=True):
    """
    -> Serve para calcular o fatorial de um número n e retornar o calculo e o resultado
    :param n: numero a ser fatoriado
    :param show: (opcional) define se vai mostrar o calculo ou não
        True = mostra calculo (padrão)
        False = não mostra o calculo
    :return: retorna o valor do Fatorial de um número n
    """
    c = n
    f = 1
    print(f' +=> Calculando {n}! = ', end='')

    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(3, show=True))
help(fatorial)