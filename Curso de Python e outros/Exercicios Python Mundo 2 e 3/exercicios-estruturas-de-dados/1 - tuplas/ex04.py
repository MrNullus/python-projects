num = (
    int(input("$ Digite um número:> ")), int(input("$ Digite mais um número:> ")),
    int(input("$ Digite outro número:> ")), int(input("$ Digite o ultimo número:> "))
)

print(f'# Os valores digitados foram: {num}')
print(f'# O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'  # O valor apareceu na posição {num.index(3) + 1}º')
else:
    print("  # O valor 3 não foi digitado")
print("  # Os números pares são: ", end=' ')

for par in num:
    if par % 2 == 0:
        print(par, end=' ')