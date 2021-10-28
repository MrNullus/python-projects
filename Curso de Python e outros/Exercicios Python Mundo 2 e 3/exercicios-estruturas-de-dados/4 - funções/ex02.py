def area(larg, comp):
    print(' ----------      ÁREA DO TERRENO    -------------')
    a = larg * comp
    print(f'- A aréa de um terreno {larg}x{comp} é de {a}m².')
    print('------------- ------- ---------- ---------- -----')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)