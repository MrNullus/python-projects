# Oi oi docinho, tá tudo bem estranho e distante entre nós, isso é uma merda e só queria dizer mesmo que: Seu sorriso e teu olhar é o que tem mais belo e verdadeiro nessa porra desse mundo todo, mesmo que sei lá sua capitalista safada a gente pare de se falar oou não veja vc mais. Ainda você vai ser um leque de emoções para mim. Essa musica é perfeita para você
# ksksksksk desculpa a hora


def valideIdade():
    from datetime import datetime
    global idade
    idade = datetime.now().year - ano


def valideVoto():
    global resp
    if idade >= 18:
        resp = "VOTA"
    elif idade >= 16 or idade < 18:
        resp = "VOTO OPCIONAL"
    else:
        resp = "NÃO VOTA"


def VotaOuNao():
    global ano
    print('-' * 30)
    ano = int(input('Em que ano você nasceu?  '))
    valideIdade()
    valideVoto()
    print(f' - Com {idade} anos : {resp}.')
    print('-' * 30)


VotaOuNao()