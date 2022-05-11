from gameEngine import *
from variables import *
from main import limoRacing

class running(limoRacing):
    def runGame(self, game_engine):
        return super().runGame(game_engine)
    
carro = running(flag_run, velocidade, contador_pitu, pitu_points, pitu_points_str, points_str, points, game_engine, flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, bitcoin, x_bitcoin, y_bitcoin)

#Definição de variavéis para o menu
pygame.init()  
res = (1263,839)  
screen = pygame.display.set_mode(res)  
color = (255,255,255)  
color_light = (170,170,170)  
color_dark = (100,100,100)  
width = screen.get_width()  
height = screen.get_height()  
smallfont = pygame.font.SysFont('Corbel',35)  
text = smallfont.render('START' , True , color)
text2 = smallfont.render('QUIT' , True , color)
flag = False
flag_quit = False
fundo = pygame.image.load('fundo.png')

while True:  
    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:  
            pygame.quit()
        
    #Criação de menu inicial com 2 opcções: START e QUIT
        if ev.type == pygame.MOUSEBUTTONDOWN:  
            if width/2 - 67 <= mouse[0] <= (width/2 + 76) and height/2 <= mouse[1] <= height/2+40:  
                flag = True  

        if ev.type == pygame.MOUSEBUTTONDOWN:  
            if width/2 - 67 <= mouse[0] <= width/2 + 76 and height/2 + 138 <= mouse[1] <= height/2 + 181:  
                flag_quit = True

    screen.blit(fundo,(0,0))  
    screen.blit(titulo, (largura/2 - 340, altura/8))
    mouse = pygame.mouse.get_pos()  
    
    if width/2 - 67 <= mouse[0] <= width/2 + 76 and height/2 <= mouse[1] <= height/2+40:  
        pygame.draw.rect(screen,color_light,[width/2 - 65 ,height/2,140,40])  
    else:  
        pygame.draw.rect(screen,color_dark,[width/2 - 65,height/2,140,40])  
    
    
    if width/2 - 67 <= mouse[0] <= width/2 + 76 and height/2 + 138 <= mouse[1] <= height/2 + 181:  
        pygame.draw.rect(screen,color_light,[width/2 - 65 ,height/2 + 140,140,40])  
    else:  
        pygame.draw.rect(screen,color_dark,[width/2 - 65,height/2 + 140,140,40])

    screen.blit(text, ((width/2) - 42,(height/2 + 4.8)))  
    screen.blit(text2, ((width/2) - 33,(height/2 + 144)))
    pygame.display.update()
    
    #Iniciação do código fonte do jogo (game_engine) e iniciação dos arquivos de música, caso o botão START do menu for ativado
    if flag == True:
        i = 0
        for b in sounds:
            i += 1
            if i == 1:
                b.play(-1).set_volume(0.02)
            elif i == 2:
                b.play(-1).set_volume(0.08)
            else:
                b.play(-1).set_volume(0.5)
        carro.runGame(game_engine)

    if flag_quit == True:
        exit()
