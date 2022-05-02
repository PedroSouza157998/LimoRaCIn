import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
points = 0
altura = 600
largura = 480
x_verde = 0
y_verde = 0
x_vermelho = randint(50,350)
y_vermelho = 100
x_amarelo = 0
y_amarelo = 0

tela = pygame.display.set_mode((altura,largura))
relogio = pygame.time.Clock()
pygame.display.set_caption('LImo RaCIn')

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x_vermelho >= 40:
                x_vermelho -= 10
            elif event.key == K_d and x_vermelho <= 560:
                x_vermelho += 10
            elif event.key == K_w and y_vermelho >= 10:
                y_vermelho -= 10
            elif event.key == K_s and y_vermelho <= 440:
                y_vermelho += 10


    if pygame.key.get_pressed()[K_a]:
        if(x_vermelho >= 10): x_vermelho -= 10
    elif pygame.key.get_pressed()[K_d]:
        if(x_vermelho <= 560): x_vermelho += 10
    elif pygame.key.get_pressed()[K_w]:
        if(y_vermelho >= 10): y_vermelho -= 10
    elif pygame.key.get_pressed()[K_s]:
        if(y_vermelho <= 440): y_vermelho += 10

    rect_verde = pygame.draw.rect(tela,(0,135,1),(x_verde,y_verde,30,30))
    rect_vermelho = pygame.draw.rect(tela,(255,0,0),(x_vermelho,y_vermelho,30,30))
    rect_amarelo = pygame.draw.rect(tela,(255,255,0),(x_amarelo,y_amarelo,30,30))
    y_verde += 4
    y_amarelo += 4

    if y_verde > altura:
        y_verde = 0
        x_verde = randint(50,350)
    if rect_verde.colliderect(rect_vermelho):
        exit()
    if y_amarelo > altura:
        y_amarelo = 0
        x_amarelo = randint(50,350)
    if rect_vermelho.colliderect(rect_amarelo):
        points+=1
        print('Pontos: ',points)
        y_amarelo = 0
        x_amarelo = randint(50,350)

    pygame.display.update()