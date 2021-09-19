import moeda

p = float(input('$ Digite o preço: R$ '))
print(f'- A metade de {moeda.m(p)} é R${moeda.m(moeda.metade(p))}')
print(f'- O dobro de {moeda.m(p)} é R${moeda.m(moeda.dobro(p))}')
print(f'- Aumentando 10% tem, R${moeda.m(moeda.aumentar(p, 10))}')
print(f'- Diminuindo 10% temos, R${moeda.m(moeda.diminuir(p, 10))}')
