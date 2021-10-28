from random import randint
computador = randint(0, 5)
acerto = False
palpites = 0

print("Olá sou o seu computador...")
while not acerto:
    print("Tente adivinhar um numero de 0 a 5")
    palpites += 1
    jogador= int(input("Qual o seu palpite? "))
    if computador == jogador:
        print("Você acertou, teve {} palpites\n Numero sorteado: {}".format(palpites, computador))
        acerto = True
    else:
        if jogador > computador:
            print("Menos...")
        elif jogador < computador:
            print("Mais....")