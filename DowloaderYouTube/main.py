#libs necessarias
import time
from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable

# funcao para escolher o que voce quer baixar
def opt_dowload():
    print("\n- Opções de dowload :3 -\n1)Baixar um video\n2)Baixar uma playlist")
    time.sleep(2)
    opt = int(input("\n- Digite a opção desejada > "))
    if opt == 1:
        baixar_video()
    elif opt == 2:
        baixar_playlist()
    elif opt != 1 and opt != 2:
        print("\n~ Essa opção não é valida ToT")

# Criar função de baixar o video
def baixar_video():
    # Criar variavel para receber a url do video
    video_url = input('$ Digite a url do video desejado > ')
    yt = YouTube(video_url)
    # verificar se o video é acessivel
    try:
        yt = YouTube(video_url)
    except VideoUnavailable:
        print(f'Video {yt} inacessivel')
    else:
        print(f'\n\tDowloading do video: {yt.title}')
        v.streams.first().download(output_path="libs/streams")
        print("\n\t~~Dowload concluido! ;3 ~~")


# criar função que vai baixar a playlist
def baixar_playlist():
    # Criar variavel que vai receber a url da playlist
    playlist_url = str(input("$ Digite a url desejada > "))
    p = Playlist(playlist_url)

    for url in p.video_urls:
        try:
            yt = YouTube(url)
        except VideoUnavailable:
            print(f'Video {url} is unavaialable, skipping.')
        else:
            print(f'Downloading video: {url}')
            yt.streams.first().download()

# funcao iniciar
def start():
    print("\n -===== BEM VINDO!! =====- ")
    time.sleep(2)
    print('\n  $_$ ~~Ao BaixaTube~~')
    time.sleep(2)
    opt_dowload()

start()