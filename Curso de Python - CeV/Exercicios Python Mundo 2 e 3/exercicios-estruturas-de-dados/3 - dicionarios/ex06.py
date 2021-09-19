galera = list()
pessoa = dict()
soma = media = 0

print("-="*30)
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:>> '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] :>> ')).upper()[0]
        if pessoa['sexo'] in 'MF' or pessoa['sexo'] in 'mf':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade:>> '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro porra! Responda S ou N')
    if resp == 'N':
        break
print("-="*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média das idades é de {media:5.1f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pesoas que estão acima da média : ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'  {k} = {v};', end='')
print()
print("-="*30)
