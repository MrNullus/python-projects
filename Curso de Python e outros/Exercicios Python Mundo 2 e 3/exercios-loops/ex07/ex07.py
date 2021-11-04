sexo = str(input("Informe seu sexo [M/F]:> ")).strip().upper()[0]
while sexo != 'm' and sexo != 'f':
    sexo = str(input("Informe seu sexo de novo ouve erro [M/F]:> ")).strip().upper()[0]
    print("Sexo invalido!")
print('Sexo {} reistrado com suceso'.format(sexo))