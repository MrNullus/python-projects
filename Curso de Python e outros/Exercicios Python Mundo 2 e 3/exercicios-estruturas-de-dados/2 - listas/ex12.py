import cad as cad

ficha = list()
while True:
    nome = str(input('Nome:>> '))
    nota1 = float(input('Nota 1:>> '))
    nota2 = float(input('Nota2:>> '))
    media = (nota1 + nota2)/2

    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar porra? [S/N] '))
    if resp in 'Nn':
        break

print('=-==-='*6)
print(f'{"No":<4}| {"NOME":<10}|  {"MÉDIA":>8}')
print('=-==-='*6)
for i, a in enumerate(ficha):
    print(f'{i:<4}| {a[0]:<10}|{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar nota de qual aluno? (999 finaliza corno) '))
    if opc == 99:
        print('Finalizando caralhos......')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print(' <<<<<   FALOU!!!   >>>>>')