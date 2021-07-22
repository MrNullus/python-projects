import time
opt = 0

print("\n====== Bem Vindo ======")
num1 = int(input("Digite o primeiro número.: "))
num2 = int(input("Digite o segundo número..: "))

while opt != 5:
    # [1] Soma [2] Multiplicar [3] Maior [4[ Novos Números [5] Sair do Programa
    print("---"* 15)
    print("Digite uma das opções a baixo\n# [1] Soma\n# [2] Multiplicar\n# [3] Maior\n# [4] Novos Números\n# [5] Sair do Programa")
    opt = int(input("$ Qual opção >>  "))
    print("---" * 15)
    if opt == 1:
        soma = num1 + num2
        resSoma = f'# A soma do número {num1} e {num2} é {soma}'
        print(resSoma)
        print("---" * 15)
    elif opt == 2:
        print("A multiplicação dos numeros {} e {} é {}".format(num1, num2, num1 * num2))
    elif opt == 3:
        if num1 > num2:
            print("O numero {} é maior que {}".format(num1, num2))
            print("---" * 15)
        else:
            print("O numero {} é maior que {}".format(num2, num1))
            print("---" * 15)
    elif opt == 4:
        print("Digite os novos números...")
        num1 = input("Digite o primeiro número.: ")
        num2 = input("Digite o segundo número..: ")
    elif opt == 5:
        break
    else:
        print('Opção invalida. Tente Novamente')
        print("-=--=-" * 10)
        time.sleep(3)
print("Opção invalida!")