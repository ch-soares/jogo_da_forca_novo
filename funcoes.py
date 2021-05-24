import requests
from unidecode import unidecode  # retira todos os acentos de uma string
from bs4 import BeautifulSoup


def escolha_da_palavra():
    """
    Escolhe a palavra para ser inicializado o jogo

    :return: str randomizada pela API 'dicionário aberto'
    """
    requisicao_palavra = requests.get('https://api.dicionario-aberto.net/random')
    resposta_palavra = requisicao_palavra.json()
    with open('palavra.txt', 'w') as palavra:
        palavra.write(resposta_palavra['word'])
    return resposta_palavra['word']


def cabecalho():
    print('=' * 55)
    print('JOGO DA FORCA'.center(55, '.'))
    print('=' * 55)
    print('Vamos Começar!!!'.center(55, ' '))
    print('-' * 55)


def dica():
    with open('palavra.txt') as palavra:
        requisicao_palavra = requests.get(f'https://api.dicionario-aberto.net/word/{palavra.read()}')
        xml = requisicao_palavra.json()
        html = xml[0]['xml']
        soup = BeautifulSoup(html, 'html.parser')
        texto = soup.find('def').text
        return texto[:texto.find('.')]


def palavra_utilizada():
    with open('palavra.txt') as palavra:
        palavra_do_arquivo = palavra.read()
        palavra_retrabalhada = unidecode(palavra_do_arquivo.upper().strip().replace('-', ''))
        return palavra_retrabalhada


def palavra_do_arquivo():
    with open('palavra.txt') as palavra:
        return palavra.read()
