from random import randint
v = 0

print("==---=== Jogo Par ou Impar ==---===")
while True:
    print('--' * 20)
    jogador = int(input("Digita um valor: "))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Impar [P/I]?")).strip().upper()
        print('--' * 20)
    print("=-= RESULTADO =-=")
    print(f'- Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print("DEU PAR" if jogador % 2 == 0 else "DEU IMPAR")
    if tipo == 'P':
        if total % 2 == 0:
            print("$ Você venceu parabens!")
            v += 1
        else:
            print("$ Eu venci, você perdeu!")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("$ Você venceu parabens!")
            v += 1
        else:
            print("$ Eu venci, você perdeu!")
            break
print('-=-' * 12)
print(f'~~ GAME OVER!\n[ VITORIAS: {v} ]')
print('-=-' * 12)