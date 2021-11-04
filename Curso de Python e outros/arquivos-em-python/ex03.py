import os

filePath = "C:/Users/POSITIVO/PycharmProjects/ExerciciosPython/cfb-exerccios/arquivos-em-python/"
nameFile = "text3.txt"

# Verifica se o path do arquivo existe
if os.path.exists(f'{filePath}{nameFile}'):
    print("Arquivo Existente!")
else:
    f = open(f'{filePath}{nameFile}', "x")
    f.close()

if os.path.exists(f'{filePath}{nameFile}'):
    os.remove(f'{filePath}{nameFile}')
else:
    print("Arquivo inexistente")
