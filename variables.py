import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice

pygame.init()

soundtracks = ['bandoleros.mp3', 'car_sound.ogg' ,'traffic_sound.mp3']
sounds=[pygame.mixer.Sound(a)for a in soundtracks]
for b in sounds:
    b.play(-1)

points = 0
points_str = str(points)
largura = 780
altura = 600
x_verde = largura/2
y_verde = altura/2
x_azul = randint(140, 629)
y_azul = -100
x_amarelo = 0
y_amarelo = 0
x_pitu = randint(140, 629)
y_pitu = -80
flag_soma = 4
x_bitcoin = randint(140, 629)
y_bitcoin = -80


tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('LImo RaCIn')
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(fonte_padrao, 60, bold=False, italic=False)
texto = fonte.render(points_str, 1,(255,255,255))
carro_verde = pygame.image.load('greenCar.png')
carro_azul = pygame.image.load('blueCar.png')
pitu = pygame.image.load('pitu.png')
background = pygame.image.load("fundo.png")	
bitcoin = pygame.image.load('bitcoin-icon.png')
