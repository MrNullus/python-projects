# Bibliotecas necessarias
import requests
import os

# Função que irá baixr os arquivos
def baixar_arquivo(url_file, endereco):
    # vai fazer a requisição ao servidor
    resposta = requests.get(url_file)
    try:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print(f'Download concluido. Salvo em | {endereco}')
    except:
        print('Uma excessão ocorreu')

# lista de arquivos
files = [
    (
        'https://ik.imagekit.io/dwei7ukbe/monalisa_xEDncUy2v.jpg',
        'jpg'
     ),
    (
        'https://math.mit.edu/classes/18.745/Notes/Lecture_1_Notes.pdf',
        'pdf'
    )
]

# diretorio para guardar os arquivos
OUTPUT_DIR = 'output'
i = 1

# vai percorrer a lista files e baixar esses arquivos
for url, type_file in files:
    nome_arquivo = os.path.join(OUTPUT_DIR, 'arquivo{}.{}'.format(i, type_file))
    baixar_arquivo(url, nome_arquivo)
    i += 1