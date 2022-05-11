from gameEngine import *
from variables import *
from main import limoRacing

class running(limoRacing):
    def runGame(self, game_engine):
        return super().runGame(game_engine)
    
carro = running(flag_batida, flag_run, velocidade, contador_pitu, pitu_points, pitu_points_str, points_str, points, game_engine, flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, bitcoin, x_bitcoin, y_bitcoin)

#Definição de variavéis para o menu
pygame.init()  
res = (1263,839)  
screen2 = pygame.display.set_mode(res)  
cor = (255,255,255)  
cor_clara = (170,170,170)  
cor_escura = (100,100,100)  
largura_2 = screen2.get_width()  
altura_2 = screen2.get_height()  
fonte_peq = pygame.font.SysFont('Corbel',35)  
text_2 = fonte_peq.render('START' , True , cor)
text_3 = fonte_peq.render('QUIT' , True , cor)
flag_copy = False
flag_quit_2 = False
fundo_2 = pygame.image.load('fundo.png')

while True:  
    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:  
            pygame.quit()
        
    #Criação de menu inicial com 2 opcções: START e QUIT
        if ev.type == pygame.MOUSEBUTTONDOWN:  
            if largura_2/2 - 67 <= mouse[0] <= (largura_2/2 + 76) and altura_2/2 <= mouse[1] <= altura_2/2+40:  
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

        if ev.type == pygame.MOUSEBUTTONDOWN:  
            if largura_2/2 - 67 <= mouse[0] <= largura_2/2 + 76 and altura_2/2 + 138 <= mouse[1] <= altura_2/2 + 181:  
                flag_quit_2 = True

    screen2.blit(fundo_2,(0,0))  
    screen2.blit(titulo, (largura/2 - 340, altura/8))
    mouse = pygame.mouse.get_pos()  
    
    if largura_2/2 - 67 <= mouse[0] <= largura_2/2 + 76 and altura_2/2 <= mouse[1] <= altura_2/2+40:  
        pygame.draw.rect(screen2,cor_clara,[largura_2/2 - 65 ,altura_2/2,140,40])  
    else:  
        pygame.draw.rect(screen2,cor_escura,[largura_2/2 - 65,altura_2/2,140,40])  
    
    
    if largura_2/2 - 67 <= mouse[0] <= largura_2/2 + 76 and altura_2/2 + 138 <= mouse[1] <= altura_2/2 + 181:  
        pygame.draw.rect(screen2,cor_clara,[largura_2/2 - 65 ,altura_2/2 + 140,140,40])  
    else:  
        pygame.draw.rect(screen2,cor_escura,[largura_2/2 - 65,altura_2/2 + 140,140,40])

    screen2.blit(text_2, ((largura_2/2) - 42,(altura_2/2 + 4.8)))  
    screen2.blit(text_3, ((largura_2/2) - 33,(altura_2/2 + 144)))
    pygame.display.update()
    
    #Iniciação do código fonte do jogo (game_engine) e iniciação dos arquivos de música, caso o botão START do menu for ativado

    if flag_quit_2 == True:
        exit()
