# No Python rotinas(funções) são declaradas pelo comando def:
# def se dá a "definição"
#   Sintaxe:>>>
#       def nomeFunção(): // deve ter os parenteses -> ()
#           <bloco de comando da função que deve estar alinhada ao função sempre>
# ! Sempre pule duas linhas depois da funçõa - Sempre coloque a função no começo do programa

"""  - EXEMPLO 1
def titulo(msg):
    print('-' * 30)
    print(f'{msg:^}')
    print('-'*30)


titulo('PROGRAMA INICIADO')

titulo('CURSO EM VIDEO')

titulo('PROGRAMA ENCERRADO')
"""


def soma(a, b):
    print(f'A = {a}\n- B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(6, 4) # deve ser passado a qunatidade certa de parametros
# soma(a=9, b=1) // Essa é a forma explicita de determinar os parametros
# soma(b=6, a=9) // Essa é também a forma explicida porém apenas com os parametros trocados de posição, pode ser feito isso
# ! Lembrando precisa explicitar para todos os parametros

#   @ Empacotamento de paramêtro @
# - Empacotamento nada mais é que uma forma que parametro receba varios valores
# - um paramettro servira como uuma tupla apra receber varios parametros
# - serve para qunato a quantiade deparametros são indefinidor

def contador(* num):
    for v in num:
        print(f'{v} ', end='')


contador(12, 4, 5)

print('-' * 30)

valores = [12,2,5,6,7]

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

dobra(valores)
print(f'{valores}')