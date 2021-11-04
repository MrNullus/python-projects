# importação das libs necessarias
from bs4 import BeautifulSoup
import requests
import pyautogui
import time

# Lista com as urls das frases
list_frases_bom_dia = [
    "https://www.42frases.com.br/frases-de-cantadas-romanticas/",
    "https://www.frasesdobem.com.br/frases-de-bom-dia",
    "https://www.pensador.com/as_melhores_frases_de_bom_dia/",
    "https://www.awebic.com/frases-de-bom-dia-para-status/",
    "https://www.belasmensagens.com.br/frases-de-bom-dia",
    "https://www.mundodasmensagens.com/frases-bom-dia/",
    "https://www.mundodasmensagens.com/frases-lindas-bom-dia/"
]

# Dicionario que vai guardar as urls das frases
urls_frases = {
    'frases_bom_dia': list_frases_bom_dia[:]
}


# Funções
def bot_spam(url, tag):
    """
    -> Funçã oque vai gerar as mensagens
    :param url: url do site a se extrair as mensagens
    :param tag: nome da tag a se pegar
    :return: sem retorno
    """

    time.sleep(2.5)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    # print(parse)
    html = parse.find_all(tag)
    print(html)
    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press("enter")
        time.sleep(2.5)


# Programa principal
for i, f in enumerate(urls_frases['frases_bom_dia']):
    bot_spam(urls_frases['frases_bom_dia'][i], 'p')
