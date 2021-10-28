def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Diite um número:>>  '))
if par(num):
    print('Éeeee paaaaaaarr!!!')
else:
    print('Nãooooo é paaarr!!!')
