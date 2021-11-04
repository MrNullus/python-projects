#  - Interising Help
# + Serve para criar uma interação de ajuda entre o usuario e a linguagem
#   +-> para isso tem o comando help() e o que você quer saber
#   +-> ou pode usar, help(comando que quer saber)

#   - DOCSTRINGS
# + São manuais que definem  o uso de comandos do Python
# + Para funções inexistente, para você criar suas funções precisa-se usar:>>
#      +->  Coloque a função dentro de comentarios para que a função tenha uma DOCSTRING.
#      +->  Assim pessoas que nao são você vai saber como usar o cmando, tornando mais util
#      +->  Para consultar a DOCSTRING use o comando:>>
#           =+> help(comando)

def contador(i, f, p):
    """ isso aqui seria uma DOCSTRING
        -> Função para contar
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
        Função de Sei Lá Quem
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fiim! .........')

help(contador) # Desde jeito que se consulta uma DOCSTRING

#      @ Escopo de Variaveis @
#  - Escopo basicamente é o lugar onde a variavel vai existir, ou seja, aonde vai ser possive, usar ou não;
#  - Exsitem dois tipos de escopo de variaveis :>>>
#      -> Escopo Glopal : Nesse escopo a variavel pode ser usada em todo o programa;
#      -> Escopo Local : Nesse escopo a variavel só existe em um determinado bloco de codigo, ou seja, não pode ser usada em todo po programa e sim apenas em seu bloco de codigo correspondente;
# - Para transformar uma variavel local em global usa-se o comando:>>
#   +-> global <variavel>

# @ Para indicar o retorno de uma variavel usa-se o comando:>>
#   +=> return <valor do retorno>
#  - a função vai gerar o retorno então para isso colocasse normalmente em variveis

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 4, 9)
r2 = somar(12, 34)
r3 = somar(34, 90, 1221)

print(f'Os resultados dassomas foram, {r1}, {r2} e {r3}.')