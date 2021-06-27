import requests
from unidecode import unidecode  # retira todos os acentos de uma string
from bs4 import BeautifulSoup


def escolha_da_palavra():
    """
    Escolhe a palavra e cria o arquivo palavra.txt na qual ela será armazenada

    :return: str randomizada pela API 'dicionário aberto'
    """
    requisicao_palavra = requests.get('https://api.dicionario-aberto.net/random')
    resposta_palavra = requisicao_palavra.json()
    with open('palavra.txt', 'w') as palavra:
        palavra.write(resposta_palavra['word'])
    return resposta_palavra['word']


def dica():
    '''
    Busca a definição da palavra escolhida
    :return: str da definição da palavra até o primeiro ponto final.
    '''
    with open('palavra.txt') as palavra:
        requisicao_palavra = requests.get(f'https://api.dicionario-aberto.net/word/{palavra.read()}')
        xml = requisicao_palavra.json()
        html = xml[0]['xml']
        soup = BeautifulSoup(html, 'html.parser')
        texto = soup.find('def').text
        return texto[:texto.find('.')]


def palavra_utilizada():
    '''
    Lê a palavra escolhida, porém trabalhada
    :return: str da palavra sem acentos, caracteres especiais e espaços
    '''
    with open('palavra.txt') as palavra:
        palavra_do_arquivo = palavra.read()
        palavra_retrabalhada = unidecode(palavra_do_arquivo.upper().strip().replace('-', ''))
        return palavra_retrabalhada


def palavra_do_arquivo():
    '''
    Lê a palavra escoliha do arquivo palavra.txt
    :return: str palavra do arquivo palavra.txt
    '''
    with open('palavra.txt') as palavra:
        return palavra.read()
