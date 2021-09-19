from random import randint

numeros = (
    randint(0, 10), randint(0, 10), randint(0, 10),
    randint(0, 10), randint(0, 10)
)

print("-= Os números sorteados foram: ", end=' ')
for n in numeros:
    print(n, end=' ')

print(f'\n# O maior número foi: {max(numeros)}')
print(f'# O menor número foi: {min(numeros)}')
