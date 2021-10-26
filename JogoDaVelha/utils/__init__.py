# Main Imports
import os
import random
from colorama import Fore

# Variaveis Globais
jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"
boardVelha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Functions
def limpaTela():
    print('\n' * 5)


def createTela():
    global boardVelha
    limpaTela()
    print(f'{Fore.RED}{"JOGO DA VELHA":^45}{Fore.RESET}')
    print(f"""{Fore.YELLOW}
            {"0":^5}    {"1":^5}   {"2":^5}
        0:  {boardVelha[0][0]:^5} | {boardVelha[0][1]:^5} | {boardVelha[0][2]:^5} 
            {"":-^23}
        1:  {boardVelha[1][0]:^5} | {boardVelha[1][1]:^5} | {boardVelha[1][2]:^5} 
            {"":-^23}
        2:  {boardVelha[2][0]:^5} | {boardVelha[2][1]:^5} | {boardVelha[2][2]:^5}  
    {Fore.RESET}""")
    print(f'Jogadas: {Fore.GREEN}{jogadas}{Fore.RESET}')


def player():
    global jogadas
    global quemJoga
    global maxJogada

    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha  >>>  "))
            c = int(input("Coluna >>>  "))
            while boardVelha[l][c] != " ":
                l = int(input("Linha  >>>  "))
                c = int(input("Coluna >>>  "))

            boardVelha[l][c] = 'X'
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha e ou coluna invalida")
            os.system("pause")


def enemy():
    global jogadas
    global quemJoga
    global maxJogada

    if (quemJoga == 1) and (jogadas < maxJogadas):
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while boardVelha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)

        boardVelha[l][c] = "O"
        jogadas += 1
        quemJoga = 2


def verificaVitoria():
    global boardVelha
    vitoria = 'n'
    simbolos = ["X", "O"]

    for s in simbolos:
        vitoria = "n"
        #Verificar linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(boardVelha[il][ic] == s):
                    soma += 1
                ic += 1
            if(soma == 3):
                vitoria = s
                break
            il += 1
        if(vitoria != "n"):
            break

        # Verificar Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (boardVelha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != 'n'):
            break

        # Verifica a diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if(boardVelha[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if(soma == 3):
            vitoria = s
            break

        # Verifica a diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if (boardVelha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria


def redefinir():
    global jogarNovamente
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    global boardVelha

    jogarNovamente = "s"
    jogadas = 0
    quemJoga = 2 # 1 - Jogador | 2 - CPU
    maxJogadas = 9
    vit = 'n'
    boardVelha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
