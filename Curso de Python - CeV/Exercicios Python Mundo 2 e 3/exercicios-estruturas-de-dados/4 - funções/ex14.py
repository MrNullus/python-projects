def notas(*n, sit=False):
    """
    -> Função para analisar notas. media e situações de varios alunos
    :param n: uma ou varias notas dos alunos
    :param sit: indica se deve adicionar a situação do aluno ou não (opcional)
        True = adiciona
        False = não adiciona
    :return: dicionario com varias infromações da turma
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = "BOA"
        elif r['média'] >= 5:
            r['situação'] = "RAZOAVEL"
        else:
            r['situação'] = "RUIM"
    return r

resp = notas(4, 3, 2, 4, sit=True)
print(resp)

# help(resp)
# help(notas)