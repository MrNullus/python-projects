times = (
    'Corintians', 'Palmeiras', 'Santos' ,'Grêmio',
    'Cruzeiro','Flamengo', 'Vasco', 'Chapecoense',
    'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
    'São Paulo', 'Fluminense', 'Sport Recife',
    'EC Viória', 'Curitiba', 'Avaí', 'Ponte Preta',
    'Atlético-GO'
)
# listas de times do Brasileirão
print(f'Os times do Brasileirão são: {times}')
print("-=-"*25)

# Cinco primeiros colocados
print(f'Cinco primeiros colocados - {times[0:5]}')
print("-=-"*25)

# Os ultímos 4 colocados
print(f'Os ultímos 4 colocados - {times[15:20]}')
print("-=-"*25)

# Tímes em ordem alfabética
print(f'Tímes em ordem alfabética - {sorted(times)}')
print("-=-"*25)

# Em que posição estiver o time da Chapecoense
print(f'A posição do Chapecoense é a: {times.index("Chapecoense") + 1}º')
print("-=-"*25)