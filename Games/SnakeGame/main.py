import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('/home/cassios/Code/Python_Projects/Games/SnakeGame/music/boxcat.mp3')
som = pygame.mixer.Sound('/home/cassios/Code/Python_Projects/Games/SnakeGame/music/sfx_alarm_loop7.wav')
musica = pygame.mixer.music
musica.play(-1)

width = 640
height = 480

snake_x = (width - 20) / 2
snake_y = (height - 20) / 2
snake_size = 5
death = False

apple_x = randint(0, width - 20)
apple_y = randint(0, height - 20)

speed = 5
speed_x = speed
speed_y = 0

screen = pygame.display.set_mode((width, height), RESIZABLE)
pygame.display.set_caption('28/12/2022')
snake_list = []


def increase(snake_body):
    for XeY in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), (XeY[0], XeY[1], 20, 20))


def restart():
    global snake_size, snake_x, snake_y, apple_x, apple_y, speed_x, speed_y, score, snake_list, death
    musica.play(-1)
    death = False
    snake_list = []
    snake_x = (width - 20) / 2
    snake_y = (height - 20) / 2

    apple_x = randint(0, width - 20)
    apple_y = randint(0, height - 20)

    speed_x = speed
    speed_y = 0
    score = 0
    snake_size = 5


clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25, True)
score = 0

while True:
    window = pygame.display.get_window_size()
    width = window[0]
    height = window[1]

    msg = f'Pontos: {score}'
    msg_lose = 'Você Perdeu aperte "R" Para continuar'
    text = font.render(msg, True, (255, 255, 255))
    text_lose = font.render(msg_lose, True, (255, 255, 255))

    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_w and speed_y != speed:
                speed_y = -speed
                speed_x = 0
            if event.key == K_s and speed_y != -speed:
                speed_y = speed
                speed_x = 0
            if event.key == K_d and speed_x != -speed:
                speed_x = speed
                speed_y = 0
            if event.key == K_a and speed_x != speed:
                speed_x = -speed
                speed_y = 0

    if snake_x > width:
        snake_x = -20
    if snake_x < -20:
        snake_x = width
    if snake_y > height:
        snake_y = -20
    if snake_y < -20:
        snake_y = height

    snake_x += speed_x
    snake_y += speed_y

    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)

    increase(snake_list)

    if len(snake_list) > snake_size:
        del snake_list[0]

    snake = pygame.draw.rect(screen, (255, 255, 255), (snake_x, snake_y, 20, 20))
    apple = pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, 20, 20))

    if snake.colliderect(apple):
        som.play()
        snake_size += 5
        score += 1
        apple_x = randint(0, width - 20)
        apple_y = randint(0, height - 20)

    if snake_list.count(snake_head) > 1:
        death = True
        while death:
            musica.stop()
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart()
            screen.blit(text_lose, (width - (width - 80), height - (height - 220)))
            pygame.display.flip()

    print(f'{width},  {height}')

    if window == (1366, 745):
        speed = 10

    c = - height + 1000

    screen.blit(text, (width - 140, c / 32))
    pygame.display.flip()
