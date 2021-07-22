print('-=-=-'*4)
print(' Gerador de PA')
print('-=-=-'*4)

primeiro = int(input('Primeiro Termo:> '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('n{} -> {} | '.format(cont, termo), end='')
        termo += razao
        cont += 1
    print('~~ PAUSA!')
    mais = int(input("+- Quantos termos você quer ver mais? "))
print("Progressão finalizada com {} termos mostrados".format(total))