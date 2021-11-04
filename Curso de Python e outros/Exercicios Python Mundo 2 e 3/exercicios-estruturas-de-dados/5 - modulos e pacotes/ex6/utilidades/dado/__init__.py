def leaiDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha():
            print(f'ERRO: \"{entrada}\" é umpreço invalido')
        else:
            valido = True
            return float(entrada)
