import PySimpleGUI as sg
import funcoes

funcoes.escolha_da_palavra()
nome_palavra = funcoes.palavra_utilizada().upper()

qtde_letras = []

for caractere in nome_palavra:
    qtde_letras.append('')

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto_escolha = {
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
        [sg.Button(f'{linha1}', size=(1, 1)) for linha1 in alfabeto[:13]],
        [sg.Button(f'{linha2}', size=(1, 1)) for linha2 in alfabeto[13::]],
        [sg.Text()],
        [sg.Button('Dica'), sg.Button('Sair do Jogo')],
        [sg.Output(size=(50, 5), key='dica')],
          ]

janela = sg.Window('JOGO DA FORCA', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Sair do Jogo':
        break
    if eventos == 'Dica':
        print(funcoes.dica())
    if eventos in nome_palavra and eventos not in letras_acertadas:
        for indice, letra in enumerate(nome_palavra):
            if eventos == letra:
                letras_acertadas.append(eventos)
                letras_acertadas.sort()
                janela[indice].update(eventos)
    if eventos not in nome_palavra and eventos in alfabeto_escolha:
        chances -= 1
        janela['chances'].update(chances)
        if chances == 0:
            sg.PopupOK('', 'Você perdeu!!')

    if eventos not in escolhas and eventos in alfabeto_escolha:
        escolhas.append(eventos)
        escolhas.sort()
        janela['escolhas'].update(escolhas)
    if len(letras_acertadas) == len(nome_palavra):
        sg.Popup('Parabéns!')
