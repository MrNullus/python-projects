# Para usar o JSON é preciso importar a lib json
import json

# Criar JSON
carros_json = '{"marca":"honda", "modelo":"HVN", "cor":"Prata"}'

# Vai carregar o json em uma variavel
carros = json.loads(carros_json)

# Pode usar todos os metodos do Dict nesa variavel agora
# Json seria como um Dict - Sendo transformado em um
#for keys, values in carros:
#    print(f'Chave: {keys} | Valor: {values}')


pessoa = {
    "nome":"Gustavo",
    "idade":12
}

# Converte um Dict num JSON
pessoas_json = json.dumps(pessoa)
print(pessoas_json)

# Pode se usar não só Dicts para transformar em json, pode usar arrays e tuplas
# Depois que são convertidas virar:
#   - Dictionary -> objeto json
dict_json = {"marca":"honda", "modelo":"HVN", "cor":"Prata"}
#   - List -> array json
lista_json = ["marca","honda", "modelo","HVN", "cor","Prata"]
#   - Tuplas -> array json
tupla_json = ("marca","honda", "modelo","HVN", "cor","Prata")

# Parametros que podem ser usados no dumps()
dict = json.dumps(dict_json, indent=4, separators=(":","="), sort_keys=True)

jogador = {
    "nome":"Gustavito",
    "time":"aviadores",
    "vivo":True,
    "energia":100,
    "mochila":[
        "reco-reco", "espada de são jorge", "cuzcuz"
    ],
    "aeronaves":[
        {
            "nome":"Carro", "tipo":"transporte", "habilidade":100
        },
        {
            "nome":"Jatinho", "tipo":"ataque", "habilidade":156
        },
        {
            "nome":"Motoca", "tipo":"fuga", "habilidade":200
        }
    ]
}

jogador2_json = '{"nome":"Fer","time":"aviadores","vivo":"True","energia":"100","mochila":["reco-reco", "espada de são jorge", "cuscuz"],"aeronaves":[{"tipo":"transporte", "habilidades":"100"},{"tipo":"ataque", "habilidades":"156"},{"tipo":"fuga", "habilidades":"200"}]}'

jogador2 = json.loads(jogador2_json)
print(jogador2)

#chaves
for keys in jogador:
    print(keys)
print("----" * 5)

#itens
for items in jogador.items():
    print(items)
print("----" * 5)

#valores
for values in jogador.values():
    print(values)
print("----" * 5)

#nome do jogador
print(jogador["nome"])
print("----" * 5)

#time jogador
print(jogador["time"])

#itens da mochila
for itemsMochila in jogador["mochila"]:
    print(itemsMochila)

#Aeronaves
print("-" * 26)
print("     Aeronaves    ")
for aeronave in jogador["aeronaves"]:
    print("-" * 26)
    print(f'Nome       - {aeronave["nome"]:>6}')
    print(f'Tipo       - {aeronave["tipo"]:>6}')
    print(f'Habilidade - {aeronave["habilidade"]:>6}')
    print("-" * 26)
