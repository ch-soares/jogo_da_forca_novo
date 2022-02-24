# Jogo adivinha a palavra

Jogo de adivinha a palavra desenvolvido em Python, com a interface gráfica PySimpleGui.


[![Build Status](https://app.travis-ci.com/ch-soares/jogo_adivinha_palavra.svg?branch=main)](https://app.travis-ci.com/ch-soares/jogo_adivinha_palavra)
[![Updates](https://pyup.io/repos/github/ch-soares/jogo_adivinha_palavra/shield.svg)](https://pyup.io/repos/github/ch-soares/jogo_adivinha_palavra/)
[![Python 3](https://pyup.io/repos/github/ch-soares/jogo_adivinha_palavra/python-3-shield.svg)](https://pyup.io/repos/github/ch-soares/jogo_adivinha_palavra/)

Versão do Python: 3.9.0

## Como desenvolver

1. Clone o repositório
2. Cria um virtualenv com Python 3.9.0
3. Ative o virtualenv
4. Instale as dependências

## Para instalar

```console
git clone git@github.com:ch-soares/jogo_adivinha_palavra.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## O jogo

* Você possui 6 chances de acertar a palavra.
* A letra escolhida é mostrada em ordem alfabética no campo "Letras escolhidas".
* A qualquer momento pode solicitar uma dica, usando o botão correspondente. 
* Tanto em caso de perda, quando exauridas as chances, quanto em caso de acerto da palavra, o jogo é reiniciado.
* Para sair, basta fechar a tela ou clicar no botão de Sair do Jogo.
      
Obs: A palavra, bem como a dica para o acerto da mesma, é gerada automaticamente por meio de uma api do português de
Portugal. Isto porque, infelizmente, não encontrei uma api pública no Brasil.
