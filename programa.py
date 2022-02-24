import requests
from unidecode import unidecode  # retira todos os acentos de uma string
from bs4 import BeautifulSoup
import PySimpleGUI as sg


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


def janela_jogo():
    '''
    Inicia o jogo
    :return: irá retornar sempre o jogo, o jogador ganhando ou perdendo
    '''
    sg.theme('Dark2')
    escolha_da_palavra()
    nome_palavra = palavra_utilizada().upper()

    qtde_letras = []

    for caractere in nome_palavra:
        qtde_letras.append('')

    ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ALFABETO_ESCOLHA = {
        'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F',
        'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
        'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
        'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        'Y': 'Y', 'Z': 'Z'
    }

    letras_acertadas = []
    escolhas = []

    chances = 6

    layout = [
        [sg.Text('A palavra é...')],
        [sg.InputText(f'{letras}', size=(3, 3)) for letras in qtde_letras],
        [sg.Text()],
        [sg.Text('Letras escolhidas:'), sg.InputText(key='escolhas')],
        [sg.Text()],
        [sg.Text('Quantidade de chances:'), sg.Text(chances, key='chances')],
        [sg.Text()],
        [sg.Text('Escolha uma letra')],
        [sg.Button(f'{linha1}', size=(1, 1)) for linha1 in ALFABETO[:13]],
        [sg.Button(f'{linha2}', size=(1, 1)) for linha2 in ALFABETO[13::]],
        [sg.Text()],
        [sg.Button('Dica'), sg.Button('Sair do Jogo')],
        [sg.Output(size=(50, 5), key='dica')],
    ]

    janela = sg.Window('JOGO ADIVINHA A PALAVRA', layout, finalize=True)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Sair do Jogo':
            break
        if eventos == 'Dica':
            print(dica())
        if eventos in nome_palavra and eventos not in letras_acertadas:
            for indice, letra in enumerate(nome_palavra):
                if eventos == letra:
                    letras_acertadas.append(eventos)
                    letras_acertadas.sort()
                    janela[indice].update(eventos)
        if len(letras_acertadas) == len(nome_palavra):
            with open('palavra.txt') as palavra:
                leitura_da_palavra = palavra.read().capitalize()
                sg.Popup(f'Parabéns, você acertou! A palavra é {leitura_da_palavra}.')
            janela.hide()
            return janela_jogo()
        if eventos not in nome_palavra and eventos in ALFABETO_ESCOLHA:
            chances -= 1
            janela['chances'].update(chances)
            if chances == 0:
                with open('palavra.txt') as palavra:
                    leitura_da_palavra = palavra.read().capitalize()
                sg.Popup(f'Que pena! A palavra era {leitura_da_palavra}.')
                janela.hide()
                return janela_jogo()

        if eventos not in escolhas and eventos in ALFABETO_ESCOLHA:
            escolhas.append(eventos)
            escolhas.sort()
            janela['escolhas'].update(escolhas)


if __name__ == '__main__':
    janela_jogo()
