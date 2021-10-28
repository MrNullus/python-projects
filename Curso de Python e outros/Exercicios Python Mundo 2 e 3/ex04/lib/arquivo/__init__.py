from ex04.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # vai ler o arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # vai abrir o arquivo e depois adicionar caso o arquivo não exista
        a.close()
    except:
        print('Houve um erro na hora da criação do arquivo !')
    else:
        print(f'O arquivo {nome} foi criado com sucesso !')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS', 'amarelo')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(arq, nome='default', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Hove um ERRO na hora de escrever os dados no arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
