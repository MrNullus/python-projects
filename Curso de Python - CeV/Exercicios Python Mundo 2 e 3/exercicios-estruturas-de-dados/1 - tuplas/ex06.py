# Programa que verifica voagais(sem acentos) dentro de uma tuplas
palavras = (
    'programar', 'python', 'mercado',
    'trabalhar', 'curso', 'estudar'
)

for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra," ",end='')
