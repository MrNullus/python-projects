print('**' * 12)
print(" Sequencia de FIBONACCI")
print('**' * 12)

n = int(input('Quantos termos vai querer?  '))
t1 = 0
t2 = 1

print("~~" * 22)
print(f'# {t1} -> {t2} ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print("-> {} ".format(t3), end='')
    cont += 1

print("-> ACABOU")
print("~~" * 22)