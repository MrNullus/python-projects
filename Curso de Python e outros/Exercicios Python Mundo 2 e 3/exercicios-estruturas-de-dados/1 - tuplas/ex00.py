#Maneiras de manipular tuplas
lanche = ('Churasco', 'Hamburguer', 'Pão com mortadela', 'Pizza')

for comida in lanche: #Essa maneira é a mais simples porém só eibe o valor sem ser a posição
    print(f'Vou comer {comida}')
print("--------------------------------------------------")
for cont in range(0, len(lanche)): #Uma outra maneira que mostra o valor e posição
    print(f'Eu vou comer {lanche[cont]} Na posição {cont}')
print("--------------------------------------------------")
for pos, comida in enumerate(lanche): #Essa maneira mostra o valor e a posição com o metodo enumerate() e a variavel pos
    print(f'Vou comer {comida} Na posição {pos}')
print("--------------------------------------------------")

#Uma função para ordenar tuplas é o sorted(), e essa função não irá mudar a tupla, vai só ordenar
print(sorted(lanche))
print("--------------------------------------------------")

#Para juntar uma tupla na outra é usado o operador +, lembrando a ordem da soma influencia na junção
a = (1,2,3,4,5)
b = (6,7,8,9,10)
c = a + b
print(c)
print(b+a)
print("--------------------------------------------------")