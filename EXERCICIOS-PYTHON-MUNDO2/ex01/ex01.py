print("==== OS 10 PRIMEIROS TERMOS DE UMA PA =====")
n1 = int(input("Digite o primeiro termo da PA:> "))
r = int(input("Digite a razão:> "))
n10 = n1 + (10-1) * r
cont = 0

print(" - Os termos são esses - ")
for c in range(n1, n10 + r, r):
    cont += 1
    print(f'n{cont} {c}', end=' | ')