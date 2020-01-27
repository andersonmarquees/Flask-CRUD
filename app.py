from flask import Flask, render_template, url_for

app = Flask(__name__)


class ListaJogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = ListaJogo('Mario Bros', 'Aventura', 'SNES')
jogo2 = ListaJogo('World of Warcraft', 'RPG', 'PC')
jogo3 = ListaJogo('Tetris', 'RPG', 'PC')

lista_jogos = [
    jogo1,
    jogo2,
    jogo3
]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Lista de Jogos', lista_jogos=lista_jogos)