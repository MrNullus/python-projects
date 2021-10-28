aluno = dict()

aluno["nome"] = str(input('Nome :>> '))
aluno["media"] = float(input(f'Média de {aluno["nome"].capitalize()} :>> '))

print(f'- Nome é igual a {aluno["nome"].capitalize()}')
print(f'- Média é igual a {aluno["media"]}')
if aluno["media"] >= 7:
    print("- Situação : Aprovado")
else:
    print("- Situação : Reprovado")

