jogador = dict()
partidas = list()
jogador['nome'] = str(input('$ Nome do jogador:>> ')).capitalize()
tot = int(input(f'$ Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'  - Quantos gols na {c+1}º partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print("=-="*10)
print(jogador)
print("=-="*10)
for k, v in jogador.items():
    print(f'Campo {k} tem o valor {v}')
print("=-="*10)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    =+> Na {i+1}º partida fez {v} gols.')
print(f'Um total de {jogador["total"]} gols.')
