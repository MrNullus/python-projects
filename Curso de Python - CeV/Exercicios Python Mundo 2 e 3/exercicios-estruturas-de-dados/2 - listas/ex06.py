exrp = str(input('# Digite a expressão::> '))
pilha = []

for simb in exrp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("- Expresão Valída!")
else:
    print("- Expressão invalída!")
print(pilha)