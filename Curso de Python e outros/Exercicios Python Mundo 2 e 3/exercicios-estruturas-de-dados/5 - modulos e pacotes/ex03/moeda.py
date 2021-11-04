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

