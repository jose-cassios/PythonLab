import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

#inicializando o pygame e o som do jogo
pygame.init()
pygame.mixer.init()

# Definindo a largura e altura da tela
width = 640 
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Pong") # Nome do jogo
paredesom = pygame.mixer.Sound("/home/cassios/Code/Python_Projects/Games/SuperPong/sounds/parede.wav")
rebatesom = pygame.mixer.Sound("/home/cassios/Code/Python_Projects/Games/SuperPong/sounds/rebater.wav")
pontuasom = pygame.mixer.Sound("/home/cassios/Code/Python_Projects/Games/SuperPong/sounds/ponto.wav")
acelerasom = pygame.mixer.Sound("/home/cassios/Code/Python_Projects/Games/SuperPong/sounds/acelera.wav")

# Posição inicial dos players
y_player1 = 230
y_player2 = 230
vel_player1 = 10
vel_player2 = 10
rebatedor = 0

# Posição inicial da bola
x_bola = width/2
y_bola = height/2
x_power = randint(40, 500)
y_power = randint(40, 300)

# Velocidade inicial da bola
vel = 5
velx_bola = vel
vely_bola = vel

# Pontuação inicial dos players
score_player1 = 0
score_player2 = 0

FPS = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 20, True, False)

# Timer
cont:int = 0
colid = False

# Loop principal do jogo
while True:
    screen.fill((0, 0, 0))

    # Configura a pontuação dos players
    text1 = fonte.render(f"Player 1: {score_player1}", True, (255, 255, 255))
    text2 = fonte.render(f"Player 2: {score_player2}", True, (255, 255, 255))
    
    FPS.tick(60) # Taxa de quadros

    # Verifica se o usuário quer sair
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # Configura a movimentação dos players
    if pygame.key.get_pressed()[K_w] and y_player1 >= 0:
        y_player1 -= vel_player1
    if pygame.key.get_pressed()[K_s] and y_player1 <= height - 40:
        y_player1 += vel_player1
    if pygame.key.get_pressed()[K_UP] and y_player2 >= 0:
        y_player2 -= vel_player2
    if pygame.key.get_pressed()[K_DOWN] and y_player2 <= height - 40:
        y_player2 += vel_player2

    # Exibe os players e a bola na tela
    player1 = pygame.draw.rect(screen, (255, 255, 255), (10, y_player1, 10, 40))
    player2 = pygame.draw.rect(screen, (255, 255, 255), (620, y_player2, 10, 40))
    bola = pygame.draw.rect(screen, (255, 255, 255), (x_bola, y_bola, 10, 10))
    powerup = pygame.draw.rect(screen, (10, 255, 10), (x_power, y_power, 60, 60))

    if bola.colliderect(powerup):
        acelerasom.play()
        colid = True
        if rebatedor == 1:
            vel_player1 = 20
        else:
            vel_player2 = 20

        cont = 0
        # if velx_bola > 0:
        #     velx_bola = vel
        #     vely_bola = -vely_bola
        # if velx_bola < 0:
        #     velx_bola = -vel
        #     vely_bola = -vely_bola 
        # acelerasom.play()
        x_power = randint(40, 500)
        y_power = randint(40, 300)

    if colid and cont < 250:
        cont += 1
    else:
        vel_player1 = 10
        vel_player2 = 10
        colid = False
        cont = 0


    # Verifica se os players pontuaram
    if x_bola >= 630:
        pontuasom.play()
        x_bola = width/2
        y_bola = height/2
        score_player1 += 1
    if x_bola <= 0:
        pontuasom.play()
        x_bola = width/2
        y_bola = height/2
        score_player2 += 1
    
    # A bola rebate no teto e no chão
    if y_bola >= 470:
        vely_bola = -vel
        paredesom.play()
    if y_bola <= 0:
        vely_bola = vel
        paredesom.play()
    
    # A bola rebate ao colidir com os players
    if bola.colliderect(player1):
        velx_bola = vel
        rebatedor = 1
        rebatesom.play()
    if bola.colliderect(player2):
        velx_bola = -vel
        rebatedor = 2
        rebatesom.play()        

    # Muda a posição da bola
    x_bola += velx_bola
    y_bola += vely_bola

    # Exibe a pontuação na tela
    screen.blit(text1, (20, 40))
    screen.blit(text2, (500, 40))
    pygame.display.flip()
