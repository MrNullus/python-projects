def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco/2
    return res


def m(preco, cifra='R$'):
    return f'{cifra}{preco:>5.2f}'.replace('.', ',')

