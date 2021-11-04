from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    "jogador 1": randint(1, 6),
    "jogador 2": randint(1, 6),
    "jogador 3": randint(1, 6),
    "jogador 4": randint(1, 6)
}
print(f'{" JOGO INICICADO ":-^36}')
print(f'{" VALORES SORTEADOS ":*^28}')
for k, v in jogo.items():
    print(f'# {k.upper()} tirou {v}')
    sleep(2)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("=======  RANKING DOS JOGADORES  =======")
for i, v in enumerate(ranking):
    print(f' {i+1}º posição - {v[0]} com {v[1]}.')
print("=======  ---------------------  =======")