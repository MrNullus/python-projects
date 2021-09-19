listagem = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 14.90,
    'Transferidor', 3.95,
    'Reguá', 5,
    'Compasso', 6,
    'Mochila', 25.99,
    'Canetas', 1.50,
    'Livro', 35.90
)
print("-==-"*11)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print("-==-"*11)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'# {listagem[pos]:.<30}', end='')
    else:
        print(f'RS{listagem[pos]:>7.2f}')
print("-==-"*11)