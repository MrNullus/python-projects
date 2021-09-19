frase = str(input("Digite uma frase:> ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print("+ O inverso da frase {} é {}".format(junto, inverso))
if inverso == frase:
    print("A frase {} é uma palíndromo".format(frase))
else:
    print("A frase {} não é um palíndromo".format(frase))