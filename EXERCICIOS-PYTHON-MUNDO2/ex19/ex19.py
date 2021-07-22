total = menor = totmil = cont = 0
barato = ' '
print('''   
  ----=================----
      LOJA HYPE DESCONTÃO
  ----=================----
''')
while True:
    print('{:-^40}'.format(' CADASTRE PRODUTOS '))
    produto = str(input("- Nome produto:> "))
    preco = float(input("- Preço: R$ "))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Tem mais produto [S/N]?  ")).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'#   Valor total da compra: R$ {total:.2f}')
print(f'#   Temos {totmil} produtos custando mais de R$ 1.000,00')
print(f'#   O produto mais barato foi {barato} custando R$ {menor:.2f}')
print("-" * 40)