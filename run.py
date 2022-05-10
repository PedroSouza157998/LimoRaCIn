from gameEngine import game_engine
from variables import *
from main import limoRacing

class running(limoRacing):
    def runGame(self, game_engine):
        return super().runGame(game_engine)
    
carro = running(velocidade, contador_pitu, pitu_points, pitu_points_str, points_str, points, game_engine, flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, bitcoin, x_bitcoin, y_bitcoin)

carro.runGame(game_engine)
