num = int(input("Digite um  número:> "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end='  ')
        tot += 1
    else:
        print("\033[31m", end='  ')

    print(f'{c}', end='')
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print("É por isso que ELE É PRIMO")
else:
    print("É por isso que ELE NÃO É PRIMO")