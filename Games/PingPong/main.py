import pygame
from pygame.locals import *
from sys import *
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load("/home/cassios/Code/Python_Projects/Games/PingPong/music/flowermusic.mp3");

width = 640
height = 480

Player1Y = (height/2) - 35
Player2Y = (height/2) - 35

Player1X = 40

Xbola = width/2
Ybola = height/2

Vybola = 6
Vxbola = 6
screen = pygame.display.set_mode((width, height), RESIZABLE)

clock = pygame.time.Clock();

scorePlayer1 = 0
scorePlayer2 = 0
font_path = '/home/cassios/Code/Python_Projects/Games/PingPong/fonts/ka1.ttf'
font_size = 25
custom_font = pygame.font.Font(font_path, font_size)
""" vel = random.random() """
pygame.mixer.music.play()

while True:
    msg1 = f"Blue {scorePlayer1}"
    msg2 = f"Red: {scorePlayer2}"
    text1 = custom_font.render(msg1, True, (0, 0, 0))
    text2 = custom_font.render(msg2, True, (0, 0, 0))
    
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            exit()
        
    if pygame.key.get_pressed()[K_w] and Player1Y > 31:
        Player1Y -= 8
    if pygame.key.get_pressed()[K_s] and Player1Y < 380:
        Player1Y += 8
    if pygame.key.get_pressed()[K_a] and Player1X > 31:
        Player1X-= 8
    if pygame.key.get_pressed()[K_d] and Player1X < 600:
        Player1X += 8
        
    if pygame.key.get_pressed()[K_UP] and Player2Y > 31:
        Player2Y -= 8
    if pygame.key.get_pressed()[K_DOWN] and Player2Y < 380:
        Player2Y += 8    
    
    background = pygame.draw.rect(screen, (129, 120, 255), (0, 20, 640, 440))
    
    bola = pygame.draw.rect(screen, (255,255,255), (Xbola, Ybola, 20, 20))
    
    divisoria = pygame.draw.rect(screen, (255,255,255), (width/2, 20, 5, 440))
    paredeCima = pygame.draw.rect(screen, (255,255,255), (0, 20, 640, 10))
    paredeBaixo = pygame.draw.rect(screen, (255,255,255), (0, 450, 640, 10))
    
    paredeLeft = pygame.draw.rect(screen, (255,255,255), (0, 20, 10, 440))
    paredeRight = pygame.draw.rect(screen, (255,255,255), (width-10, 20, 10, 440))
    
    player1 = pygame.draw.rect(screen, (0,0,255), (Player1X, Player1Y, 20, 70))
    player2 = pygame.draw.rect(screen, (255,0,0), (width - 60, Player2Y, 20, 70))
        
    if bola.colliderect(paredeLeft):
        scorePlayer2+=1
        Xbola = width/2
        Ybola = height/2
        Vxbola = abs(Vxbola)
    if bola.colliderect(paredeRight):
        scorePlayer1+=1
        Xbola = width/2
        Ybola = height/2
        Vxbola = -abs(Vxbola)
        
    if bola.colliderect(paredeCima) or bola.colliderect(paredeBaixo):
        Vybola = -Vybola

    if bola.colliderect(player1) or bola.colliderect(player2):
        Vxbola = -Vxbola
        
    Xbola += Vxbola;
    Ybola += Vybola;
    
    
    screen.blit(text1, [20, 40])
    screen.blit(text2, [490, 40])
    pygame.display.flip()
