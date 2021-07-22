print('-=-=-'*4)
print(' Gerador de PA')
print('-=-=-'*4)
primeiro = int(input('Primeiro Termo:> '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('n{} -> {} |'.format(cont, termo), end='')
    termo += razao
    cont += 1
print('FIM!')