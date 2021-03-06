import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice

pygame.init()

#Para os sons tocarem ao mesmo tempo:
soundtracks = [ './musicas/car_sound.wav', './musicas/bandoleros.wav', './musicas/traffic_sound.wav']
sounds = [pygame.mixer.Sound(a) for a in soundtracks]

#Variáveis que serão utilizadas para a lógica do jogo em (game_engine)
pitu_points = 0
pitu_points_str = str(pitu_points)
points = 0
points_str = str(points)
largura = 1263
altura = 839
x_verde = largura/2
y_verde = altura - 200
x_azul = randint(305,916)
y_azul = -300
x_amarelo = 0
y_amarelo = 0
x_pitu = randint(305,916)
y_pitu = -360
flag_soma = 6
velocidade = 9
x_bitcoin = randint(305,916)
y_bitcoin = -360
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
flag_run = True
fundo_2 = pygame.image.load('./imagens/fundo.png')
flag_batida = False

pygame.display.set_caption('LImo RaCIn')
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(fonte_padrao, 60, bold=False, italic=False)
texto = fonte.render(points_str, 1,(255,255,255))
contador_pitu = fonte.render(pitu_points_str, 1,(255,255,255))
carro_verde = pygame.image.load('./imagens/greenCar.png')
carro_azul = pygame.image.load('./imagens/blueCar.png')
pitu = pygame.image.load('./imagens/pitu.png')
background = pygame.image.load("./imagens/fundo.png")	
bitcoin = pygame.image.load('./imagens/bitcoin-icon.png')
titulo = pygame.image.load('./imagens/titulo_foto.png')
