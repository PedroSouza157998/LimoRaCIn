from gameEngine import game_engine
from variables import *

class limoRacing:
    def __init__(self, *argv):
        for arg in argv:
            self.arg = arg


    # def __init__(self, game_engine, flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu):
    #     self.game_engine = game_engine
    #     self.flag_soma = flag_soma
    #     self.background = background
    #     self.pitu = pitu
    #     self.carro_azul = carro_azul
    #     self.carro_verde = carro_verde
    #     self.texto = texto
    #     self.fonte = fonte
    #     self.fonte_padrao = fonte_padrao
    #     self.relogio = relogio
    #     self.tela = tela
    #     self.x_verde = x_verde
    #     self.y_verde = y_verde
    #     self.x_azul = x_azul
    #     self.y_azul = y_azul
    #     self.x_pitu = x_pitu
    #     self.y_pitu = y_pitu 
    
    def runGame(self, game_engine):
        return game_engine(flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, x_bitcoin, y_bitcoin, bitcoin)
         
 
