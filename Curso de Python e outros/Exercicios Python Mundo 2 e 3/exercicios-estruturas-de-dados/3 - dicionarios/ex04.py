from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome:>> ')).capitalize()
nasc = int(input('Ano de Nascimento:>> '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):>> '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação:>> '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentatoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print("+=-====-=+"*4)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')
print("+=-====-=+"*4)
