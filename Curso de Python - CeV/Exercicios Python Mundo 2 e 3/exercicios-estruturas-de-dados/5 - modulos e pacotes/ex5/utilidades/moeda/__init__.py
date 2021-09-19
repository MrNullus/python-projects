def aumentar(preco, taxa, formato=False):
    res = preco + (preco * taxa/100)
    return res if not formato else m(res)


def diminuir(preco, taxa, formato=False):
    res = preco - (preco * taxa/100)
    return res if not formato else m(res)


def dobro(preco, formato=False):
    res = preco * 2
    return res if not formato else m(res)


def metade(preco, formato=False):
    res = preco/2
    return res if not formato else m(res)


def m(preco, cifra='R$'):
    return f'{cifra}{preco:>5.2f}'.replace('.', ',')


def resumo(preco, taxaa=10, taxar=5):
    print('-'*48)
    print('RESUMO DO VALOR'.center(48))
    print('-' * 48)
    print(f'# Valor digitado :\t\t{m(preco)}')
    print(f'# Dobro do valor :\t\t{dobro(preco, True)}')
    print(f'# Metade do valor :\t\t{metade(preco, True)}')
    print(f'# {taxaa}% de aumento :\t\t{aumentar(preco, taxaa, True)}')
    print(f'# {taxar}% de redução :\t\t{diminuir(preco, taxar, True)}')
    print('-' * 48)

    