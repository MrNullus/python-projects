from datetime import date
totmaior = 0
totmenor = 0

for c in range(1,8):
    atual = date.today().year
    nasc = int(input("# Em que ano a {}ª pessoa nasceu? ".format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print("- Chegaram na maioridade {} pessoas\n- São menores de idade {} pessoas".format(totmaior,totmenor))