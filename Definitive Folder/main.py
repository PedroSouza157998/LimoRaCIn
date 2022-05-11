from gameEngine import game_engine
from variables import *

class limoRacing:
    def __init__(self, *argv):
        for arg in argv:
            self.arg = arg
    
    def runGame(self, game_engine):
        return game_engine(flag_batida, flag_run, velocidade, contador_pitu, pitu_points, pitu_points_str, points_str,points, flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, x_bitcoin, y_bitcoin, bitcoin)
