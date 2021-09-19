import moeda

p = float(input('$ Digite o preço: R$ '))
print(f'- A metade de R${p} é R${moeda.metade(p):.2f}')
print(f'- O dobro de R${p} é R${moeda.dobro(p):.2f}')
print(f'- Aumentando 10% tem, R${moeda.aumentar(p, 10):.2f}')
print(f'- Diminuindo 10% temos, R${moeda.diminuir(p, 10):.2f}')
