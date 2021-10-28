# Exercicio da pasta de exceção de erros
from time import sleep
from ex04.lib.arquivo import *
from ex04.lib.interface import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('SISTEMA ARQUIVO v1.0', 'roxo')

while True:
    resposta = menu(['Ver pesssoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
         # listar conteúdo de um arquivo !
         lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro', 'azul')
        nome = str(input('Nome:  '))
        idade = leiaInt('Idade:   ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até mais!', 'vermelho')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
    sleep(1.5)
