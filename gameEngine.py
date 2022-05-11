from variables import *

pygame.init()  
res = (1263,839)  
screen3 = pygame.display.set_mode(res)  
cor = (255,255,255)  
cor_light = (170,170,170)  
cor_dark = (100,100,100)  
largura_3 = screen3.get_width()  
altura_3 = screen3.get_height()  
fonte_pe = pygame.font.SysFont('Corbel',35)  
text_2 = fonte_pe.render('START' , True , cor)
text_3 = fonte_pe.render('QUIT' , True , cor)
flag_cop = False
flag_quit_0 = False
fundo_3 = pygame.image.load('./imagens/fundo.png')
flag_batida = False

def game_engine(flag_batida, flag_run, velocidade, contador_pitu, pitu_points, pitu_points_str, points_str, points, flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, x_bitcoin, y_bitcoin, bitcoin):
    while flag_run == True:
        points_str = str(points)
        pitu_points_str = str(pitu_points)
        texto = fonte.render(points_str, 1,(255,255,255))
        contador_pitu = fonte.render(pitu_points_str, 1,(255,255,255))
        relogio.tick(60)
        tela.fill((0, 0, 0))
        tela.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a and x_verde >= 285:
                    x_verde -= 10
                elif event.key == K_d and x_verde <= 916:
                    x_verde += 10
                elif event.key == K_w and y_verde >= 10:
                    y_verde -= 10
                elif event.key == K_s and y_verde <= 685:
                    y_verde += 10

    #Define a movimentação do carro verde, respeitando os limites da estrada da imagem de fundo
        if pygame.key.get_pressed()[K_a]:
            if(x_verde >= 285): x_verde -= velocidade
        elif pygame.key.get_pressed()[K_d]:
            if(x_verde <= 916): x_verde += velocidade
        elif pygame.key.get_pressed()[K_w]:
            if(y_verde >= 10): y_verde -= velocidade
        elif pygame.key.get_pressed()[K_s]:
            if(y_verde <= 685): y_verde += velocidade

    #calls game_Screen
        tela.blit(carro_verde,(x_verde,y_verde))
        tela.blit(carro_azul,(x_azul,y_azul))
        tela.blit(pitu,(x_pitu,y_pitu))
        tela.blit(contador_pitu,(75,180))
        tela.blit(pitu, (15, 155))
        tela.blit(bitcoin,(10,55))
        tela.blit(texto,(75,65))
        tela.blit(bitcoin,(x_bitcoin, y_bitcoin))
        y_azul += flag_soma
        y_pitu += flag_soma
        y_bitcoin += flag_soma
    
    #Condicionao para que, se os objetos interativos passarem do limite inferior, voltam para cima
        if y_azul > altura:
            y_azul = -100
            x_azul = randint(285,916)
        if y_pitu > altura:
            y_pitu = -80
            x_pitu = randint(300,916)
        if y_bitcoin > altura:
            y_bitcoin = -70
            x_bitcoin = randint(305,916)

    #Definição da colisão com o carro azul, resultando no fim do jogo
        if y_verde < (y_azul + 120):
            if y_verde < y_azul - 150:
                pass
            else:
                if (x_verde > x_azul and x_verde < (x_azul + 55)) or ((x_verde + 55) > x_azul and (x_verde + 55) < (x_azul + 55)):
                    flag_batida = True
                            
    #Definição da coleta da PITU, resultando nom incremento nas velocidades dos objetoss interativos
        if y_verde < (y_pitu + 71):
            if y_verde < y_pitu - 150:
                pass
            else:
                if (x_verde > x_pitu and x_verde < (x_pitu + 65)) or ((x_verde + 75) > x_pitu and x_verde < x_pitu):
                    y_pitu = -80
                    x_pitu = randint(300,916)
                    flag_soma += 0.3
                    velocidade += 0.05
                    pitu_points += 1

    #Definição da coleta do bitcoin resultando em um som e um incremento nos pontos    
        if y_verde < (y_bitcoin + 40):
            if y_verde < y_bitcoin - 150:
                pass
            else:
                if (x_verde > x_bitcoin and x_verde < (x_bitcoin + 45)) or ((x_verde + 60) > x_bitcoin and x_verde < x_bitcoin):
                    y_bitcoin = -70
                    x_bitcoin = randint(305,916)
                    
                    barulho_moeda = pygame.mixer.music.load('./musicas/coin_sound.wav')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.1)
                    
                    points += 1
            
        while flag_batida == True:    
            for ev in pygame.event.get():  
                screen3.blit(fundo_2,(0,0))  
                screen3.blit(titulo, (largura/2 - 340, altura/8))
                screen3.blit(contador_pitu,(largura_3/2 - 70 ,altura_3/2 + 45))
                screen3.blit(pitu, (largura_3/2 - 130 ,altura_3/2 + 20))
                screen3.blit(bitcoin,(largura_3/2 + 25 ,altura_3/2 + 35))
                screen3.blit(texto,(largura_3/2 + 95 ,altura_3/2 + 45))
                mouse = pygame.mouse.get_pos()
                            
                if ev.type == pygame.QUIT:  
                    pygame.quit()
                                                
                pygame.display.update()
        pygame.display.update()
        flag_quit_2 = True