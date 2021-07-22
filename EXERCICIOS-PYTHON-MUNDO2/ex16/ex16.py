while True:
    print("=====  TABUADA VS3.0  ======")
    n = int(input("# Digite um número para saber sua tabuada: "))
    print('-'*20)
    if n < 0:
        print("VALOR INCORRETO!")
        break
    for x in range(0, 11):
        print(f'{n:2} X {x:2} = {n * x:2}')
    print('-' * 20)

print("Programa ACABOU! Até mais ><")
print('-' * 20)