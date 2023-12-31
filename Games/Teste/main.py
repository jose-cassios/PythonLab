import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
pygame.mixer.init()

diretorioPrincipal = os.path.dirname(__file__)
diretorioImagens = os.path.join(diretorioPrincipal, 'images')
diretorioSons = os.path.join(diretorioPrincipal, 'sounds')
diretorioFonts = os.path.join(diretorioPrincipal, 'fonts')

somColisao = pygame.mixer.Sound(os.path.join(diretorioSons, 'death_sound.wav'))
colidiu = False
somScore = pygame.mixer.Sound(os.path.join(diretorioSons, 'score_sound.wav'))

width = 640
height = 480
vel = 5

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprites")

black = (0, 0, 0)
white = (255, 255, 255)

spriteSheet = pygame.image.load(os.path.join(diretorioImagens, 'dinoSpritesheet.png')).convert_alpha()

score = 0

def exibeText(msg, tamanho, pos=[]):
    msg = f"{msg}"
    custom_font = pygame.font.Font(os.path.join(diretorioFonts, 'ka1.ttf'), tamanho)
    text = custom_font.render(msg, True, (black))
    screen.blit(text, pos)
    
obstaculos = choice([0, 1])

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorioSons, 'jump_sound.wav'))
        self.sprites = []
        
        for i in range(3):
            img = spriteSheet.subsurface((i*32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.sprites.append(img)

        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (90, 270)
        self.pulando = False
        
    def pular(self):
        self.som_pulo.play()
        self.pulando = True
    
    def update(self):
        if self.pulando == True:
            self.rect.y -= 5
            if self.rect.y <= 250:
                self.pulando = False
        
        if  self.rect.y < 370 and self.pulando == False:
            self.rect.y += 5
        
        if self.index > 2:
            self.index = 0
        self.index += 0.25
        self.image = self.sprites[int(self.index)]
    
class DinoVoador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        for i in range(3, 5):
            img = spriteSheet.subsurface((i*32, 0), (32, 32))
            img = pygame.transform.scale(img, (3*32, 3*32))
            self.sprites.append(img)
            
        self.index = 0
        self.image = self.sprites[self.index]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = obstaculos
        self.rect = self.image.get_rect()
        self.rect.center = (width, 300)
        self.rect.x = width
        
    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = width
            self.rect.x -= vel

            # Animation
            if self.index > 1:
                self.index = 0
            self.index += 0.125
            self.image = self.sprites[int(self.index)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((7*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = width - randrange(30, 300, 90)
    
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = width
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= vel
        
class Chao(pygame.sprite.Sprite):
    def __init__(self, i):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((6*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (2*32, 2*32))
        self.rect = self.image.get_rect()
        self.rect.y = height - 64
        self.rect.x = 64*i

    def update(self):
        if self.rect.topright[0] <= 0:
            self.rect.x += width + 64
        self.rect.x -= vel

class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((5*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (2*32, 2*32))
        self.rect = self.image.get_rect()
        self.escolha = obstaculos
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (width, height - 64)
        self.rect.x = width
    
    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = width
            self.rect.x -= vel

todas_as_sprites = pygame.sprite.Group()

dino = Dino()
dinoVoador = DinoVoador()
todas_as_sprites.add(dino, dinoVoador)

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range((640//64)+1):
    chao = Chao(i)
    todas_as_sprites.add(chao)

cacto = Cacto()
todas_as_sprites.add(cacto)
grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto, dinoVoador)

def gameOver():
    exibeText("Game Over", 25, [230, 210])
    exibeText("Pressione R para reiniciar", 20, [130, 250])
    
def reset():
    global score, obstaculos, vel, colidiu
    
    dino.rect.y = 370
    dino.pulando = False
    dinoVoador.rect.x = width
    cacto.rect.x = width
    obstaculos = choice([0, 1])
    score = 0
    vel = 5
    colidiu = False

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP and dino.rect.y == 370 and not colidiu:
                dino.pular()
            if event.key == K_r and colidiu == True:
                reset()
                
        
    colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)
    todas_as_sprites.draw(screen)
    
    if cacto.rect.topright[0] <= 0 or dinoVoador.rect.topright[0] < 0:
        obstaculos = choice([0, 1])
        cacto.rect.x = width
        dinoVoador.rect.x = width
        cacto.escolha = obstaculos
        dinoVoador.escolha = obstaculos
        
    if colisoes:
        gameOver()
        if colidiu == False:
            somColisao.play()
        colidiu = True
        pass
    else:
        score += 0.5
        todas_as_sprites.update()
    
    if (score % 100) == 0 and not colidiu:
        if vel <= 23:
            vel += 1
        somScore.play()
    
    exibeText(int(score), 25, [20, 40])
    pygame.display.flip()