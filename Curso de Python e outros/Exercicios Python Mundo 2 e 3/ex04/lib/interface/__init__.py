fonte = {
    'none'     : '\033[0;0m',   # 0 - sem cores
    'vermelho' : '\033[1;91m',  # 1 - vermelho
    'verde'    : '\033[1;32m',  # 2 - verde
    'amarelo'  : '\033[1;93m',  # 3 - amarelo
    'azul'     : '\033[1;94m',  # 4 - azul
    'roxo'     : '\033[1;35m',  # 5 - roxo
    'branco'   : '\033[1;97m',   # 6 - branco
    'cinza'    : '\033[1;37m'   # 7 - cinza
}

def leiaInt(msg):
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
        print('\033[31m -> ERRO: mané digite um número inteiro válido. \033[m')
        # esse comando serve para continuar
        # continue
    except (KeyboardInterrupt):
        print('\033[31 -> Entrada de dados interrompida pelo usuario sacopela.\033[m')
        return 0
    else:
        return n


def linha(tam=42):
    return '-' * tam

def cabecalho(txt, cor='none'):
    print(fonte[cor], end='')
    print(linha())
    print(txt.center(42))
    print(linha())
    print(fonte['none'], end='')

def menu(lista):
    cabecalho('MENU PRINCIPAL', 'vermelho')

    c = 1
    for item in lista:
        print(f'\033[1;93m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(fonte['vermelho'], end='')
    print(linha())
    print(fonte['none'], end='')
    opc = leiaInt('\033[32mSua Opção: \033[m')

    return opc
