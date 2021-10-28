def leiaInt(msg):
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
        print('\033[31m -> ERRO: mané digite um número inteiro válido. \033[m')
        # esse comando serve para continuar
        # continue
    except (KeyboardInterrupt):
        print('\033[31 -> Entrada de dados interropida pelo usuario sacopela.\033[m')
        return 0
    else:
        return n

def leiaFloat(msg):
    try:
        n = float(input(msg))
    except (ValueError, TypeError):
        print('\033[31m -> ERRO: mané digite um número real válido. \033[m')
    except (KeyboardInterrupt):
        print('\033[31 -> Entrada de dados interropida pelo usuario sacopela.\033[m')
        return 0
    else:
        return n