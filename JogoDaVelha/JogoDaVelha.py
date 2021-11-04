# Import Utils
import utils
from utils import jogadas, maxJogadas, jogarNovamente

# Main loop
while jogarNovamente == "s":
    while True:
        utils.createTela()
        utils.player()
        utils.enemy()
        utils.createTela()
        vit = utils.verificaVitoria()
        if (vit != 'n') or (jogadas >= maxJogadas):
            break

    print(f'{utils.Fore.RED}FIM DE JOGO{utils.Fore.YELLOW}')
    if (vit == "X") or (vit == "O"):
        print(f'Resultado: Jogador {vit} venceu!')
    else:
        print('Resultado: Empate!')

    jogarNovamente = input(f'{utils.Fore.BLUE}Jogar Novamente? [s/n] {utils.Fore.RESET}').strip().lower()[0]
    utils.redefinir()
