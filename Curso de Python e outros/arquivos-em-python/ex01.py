#+ Função para mexer com arquivos
#   open(<caminho file>, <metodo de abertura>)
file = open("C:/Users/POSITIVO/PycharmProjects/ExerciciosPython/cfb-exerccios/arquivos-em-python/text.txt","at")
#+ Metodos do open:
#   r - read - abrir para leitura
#   a - append - anexar
#   w - write - escrita
#   x - create - criar
#   t - text - texto
#   b - binary - binario

txt = input("Digite um texto >>>  ")

file.write(f'{txt}\n')
file.write("Fucking code !!! \nChupe Ass C++!")
file.write(":)")
file.write(f'{txt}')

file.close()
# Vai fechar o arquivo tem que fechar