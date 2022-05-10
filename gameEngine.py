from variables import *


def game_engine(flag_soma, background, pitu, carro_azul, carro_verde, texto, fonte, fonte_padrao, relogio, tela, x_verde, y_verde, x_azul, y_azul, x_pitu, y_pitu, x_bitcoin, y_bitcoin, bitcoin):
    while True:
        relogio.tick(60)
        tela.fill((0, 0, 0))
        tela.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a and x_verde >= 140:
                    x_verde -= 10
                elif event.key == K_d and x_verde <= 629:
                    x_verde += 10
                elif event.key == K_w and y_verde >= 10:
                    y_verde -= 10
                elif event.key == K_s and y_verde <= 450:
                    y_verde += 10

    #Define a movimentação do carro verde, respeitando os limites da estrada da imagem de fundo
        if pygame.key.get_pressed()[K_a]:
            if(x_verde >= 140): x_verde -= 9
        elif pygame.key.get_pressed()[K_d]:
            if(x_verde <= 629): x_verde += 9
        elif pygame.key.get_pressed()[K_w]:
            if(y_verde >= 10): y_verde -= 9
        elif pygame.key.get_pressed()[K_s]:
            if(y_verde <= 450): y_verde += 9

    #calls game_Screen
        tela.blit(carro_verde,(x_verde,y_verde))
        tela.blit(carro_azul,(x_azul,y_azul))
        tela.blit(pitu,(x_pitu,y_pitu))
        tela.blit(texto,(440,10))
        tela.blit(bitcoin,(x_bitcoin, y_bitcoin))
        y_azul += flag_soma
        y_pitu += 9
        y_bitcoin += 9
    #Condicionao para que, se os objetos interativos passarem do limite inferior, volta para cima

        if y_azul > altura:
            y_azul = -100
            x_azul = randint(160,629)
        if y_pitu > altura:
            y_pitu = -80
            x_pitu = randint(160,629)
        if y_bitcoin > altura:
            y_bitcoin = -70
            x_bitcoin = randint(160, 629)

        if y_verde < (y_azul + 120):
            if y_verde < y_azul - 150:
                pass
            else:
                if (x_verde > x_azul and x_verde < (x_azul + 55)) or ((x_verde + 55) > x_azul and (x_verde + 55) < (x_azul + 55)):
                    exit()

        if y_verde < (y_pitu + 71):
            if y_verde < y_pitu - 150:
                pass
            else:
                if (x_verde > x_pitu and x_verde < (x_pitu + 65)) or ((x_verde + 75) > x_pitu and x_verde < x_pitu):
                    y_pitu = -80
                    x_pitu = randint(160,629)
                    flag_soma += 0.7
        
        if y_verde < (y_bitcoin + 40):
            if y_verde < y_bitcoin - 150:
                pass
            else:
                if (x_verde > x_bitcoin and x_verde < (x_bitcoin + 45)) or ((x_verde + 60) > x_bitcoin and x_verde < x_bitcoin):
                    y_bitcoin = -70
                    x_bitcoin = randint(160,629)
                    
                    barulho_moeda = pygame.mixer.music.load('coin_sound.wav')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.1)
                    
        pygame.display.update()             
