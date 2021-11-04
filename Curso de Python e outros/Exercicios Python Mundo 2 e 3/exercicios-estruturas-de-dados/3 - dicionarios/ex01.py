# * Dictionarys - Dicionarios
#   - Duas formas de declaração de dicionarios
#       dict()
#       {} -> usando as chaves
"""
   # Sintaxe dos dictionarys:>>
        nome_dict = {
         (  chave1 : 'valor1', ) -> item
            chave2 : 'valor2',
            chave3 : 'valor3'
        }
"""

pessoas = {
    'nome':'Gustavo',
    'sexo':'M',
    'idade':22
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys()) # Mostra as chaves do dicionarios
print(pessoas.values()) # Mostra os valores
print(pessoas.items()) # Mostra os itens

for k, v in pessoas.items():
    print(f'- {k} = {v}')

del pessoas["sexo"]

for k, v in pessoas.items():
    print(f'- {k} = {v}')

# Listas com Dicionarios
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa:>> "))
    estado['sigla'] = str(input("Sigla do Estado:>> "))
    brasil.append(estado.copy()) # copy() -> serve para copiar um dicionario
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem como valor {v}')