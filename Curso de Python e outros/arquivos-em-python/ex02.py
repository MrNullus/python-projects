import re

file = open("C:/Users/POSITIVO/PycharmProjects/ExerciciosPython/cfb-exerccios/arquivos-em-python/text2.txt","rt")

# lê o arquivo
#print(file.read())

#print(file.read(10)) // vai ler só 12 caracteres

#print(file.readline()) // vai ler as linhas
#print(file.readline())
#print(file.readline())

#for line in file:   //percorre o arquivo
#    print(line)

res = re.sub(" ", "-", file.readline())
file.close()


print(res)

# Quanto se usa "w" ou "wt" o arquivo é reescrito perdendo seu conteudo
file = open("C:/Users/POSITIVO/PycharmProjects/ExerciciosPython/cfb-exerccios/arquivos-em-python/text2.txt","wt")
file.write(res)

file.close()
