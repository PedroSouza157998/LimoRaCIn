from gameEngine import *
from variables import *
from main import limoRacing
from menu import * 

class running(limoRacing):
    def runGame(self, menu):
        return super().runGame(menu)
    
carro = running(res, screen, color, color_light, color_dark, width, height, smallfont, text, text2, flag, flag_quit, fundo, game_engine, flag_run, velocidade, contador_pitu, pitu_points, pitu_points_str, points_str, points, flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, x_bitcoin, y_bitcoin, bitcoin)

#Definição de variavéis para o menu
