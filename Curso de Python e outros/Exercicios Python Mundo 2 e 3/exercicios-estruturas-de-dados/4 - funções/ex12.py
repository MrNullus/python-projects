def ficha(jog='<desconhecido>', g=0):
    print(f'- O jogador {jog} fez {g} gol(s)')

nome = str(input('  Nome do jogador:>> '))
gols = int(input('  Número de gols:>>  '))

if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
