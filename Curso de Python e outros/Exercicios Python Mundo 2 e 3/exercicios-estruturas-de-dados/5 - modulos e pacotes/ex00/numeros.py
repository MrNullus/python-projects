#   import nome_modulo //Serve para importar modulos
#   from nome_modulo import modulo_especifico // Serve para importar modulos specificos
#   from nome_modulo import modulo_especifico1, modulo_especifico2 // Serve para importar varios modulos epecificos
"""
    @ Pacotes
        -> Pacotes são modulos dentro de modulos, seriam vaios modulos
        -> Para criar pacotes é só criar pastas dentro de pastas, toda pasta é um modulo
        -> Em todo pacote pode ter ou não um arquivo com nome moeda.py, para que funcione
"""

from uteis import numeros

numero = int(input('Digite um número para saber seu fatorial:>> '))
fat = numeros.fatorial(numero)
print(f'- O fatorial de {numero} é de {fat}')
print(f'- O dobro de {numero} é de {numeros.dobro(numero)}')
print(f'- O triplo de {numero} é de {numeros.triplo(numero)}')
