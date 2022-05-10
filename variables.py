import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice

pygame.init()
# sound1=pygame.mixer.Sound("sound.wav")
# sound1.set_volume(1.0)
# print sound1.get_volume()
# sound1.play()
soundtracks = ['bandoleros.wav', 'car_sound.wav' ,'traffic_sound.wav']
sounds=[pygame.mixer.Sound(a) for a in soundtracks]
i = 0
for b in sounds:
    i += 1
    if i != 2:
        b.play(-1).set_volume(0.1)
    else:
        b.play(-1).set_volume(0.05)

pitu_points = 0
pitu_points_str = str(pitu_points)
points = 0
points_str = str(points)
largura = 1263
altura = 839
x_verde = largura/2
y_verde = altura/2
x_azul = randint(305,916)
y_azul = -100
x_amarelo = 0
y_amarelo = 0
x_pitu = randint(305,916)
y_pitu = -80
flag_soma = 6
velocidade = 9
x_bitcoin = randint(305,916)
y_bitcoin = -80


tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('LImo RaCIn')
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(fonte_padrao, 60, bold=False, italic=False)
texto = fonte.render(points_str, 1,(255,255,255))
contador_pitu = fonte.render(pitu_points_str, 1,(255,255,255))
carro_verde = pygame.image.load('greenCar.png')
carro_azul = pygame.image.load('blueCar.png')
pitu = pygame.image.load('pitu.png')
background = pygame.image.load("fundo.png")	
bitcoin = pygame.image.load('bitcoin-icon.png')
