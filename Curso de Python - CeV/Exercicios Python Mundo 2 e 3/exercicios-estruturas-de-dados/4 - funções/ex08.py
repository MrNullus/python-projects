def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um numero :>>>  '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(9)
f3 = fatorial(540)
print(f'Os fatorial são : {f1}, {f2} e {f3}')