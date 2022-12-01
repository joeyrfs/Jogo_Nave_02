from random import randint
import pygame
from pygame import font
from pygame import display
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame.time import Clock
import sys

pygame.init()

tamanho = 800, 600
fonte = font.SysFont('comicsans', 40)
fonte_perdeu = font.SysFont('comicsans', 100)

superficie = display.set_mode(size=tamanho, display=0)

display.set_caption('Torradas espaciais')

fundo = scale(load('images/space.jpg'), tamanho)

class Dunofausto(Sprite):
    def __init__(self, torradas):
        super().__init__()

        self.image = load('images/dunofausto_small.png')
        self.rect = self.image.get_rect()
        self.torradas = torradas
        self.velocidade = 2

    def tacar_torradas(self):
        if len(self.torradas) < 15:
            self.torradas.add(
                Torrada(*self.rect.center)
            )

    def update(self):
        keys = pygame.key.get_pressed()

        torradas_fonte = fonte.render(
            f'Torradas: {15 - len(self.torradas)}',
            True,
            (255, 255, 255)
        )
        superficie.blit(torradas_fonte,(20,20))
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.velocidade

class Torrada(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load('images/toast_small.png')
        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        self.rect.x += 1
        
        if self.rect.x > tamanho[0]:
            self.kill()

class Virus(Sprite):
    def __init__(self):
        super().__init__()

        self.image = load('images/inimigo_1.png')
        self.rect = self.image.get_rect(
            center=(800, randint(20,580))
        )

    def update(self):
        global perdeu
        self.rect.x -= 0.1    

        if self.rect.x == 0:
            self.kill()
            perdeu = True

grupo_inimigos = Group()
grupo_torradas = Group()
dunofausto = Dunofausto(grupo_torradas)
grupo_duno = GroupSingle(dunofausto)

grupo_inimigos.add(Virus())

clock = Clock()
mortes = 0
round = 0
perdeu = False

fundoX = tamanho[0]

while True:
    # loop de eventos

    clock.tick(120)  # FPS
    
    if round % 120 == 0:
        if mortes < 20:
            grupo_inimigos.add(Virus())
        for i in range(int(mortes / 20)):
            grupo_inimigos.add(Virus())

    # Espaço dos eventos
    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == KEYUP:
            if evento.key == K_SPACE:
                dunofausto.tacar_torradas()

    if groupcollide(grupo_torradas, grupo_inimigos, True, True):
        mortes += 1

    # Espaço do display
    superficie.blit(fundo,(0,0))

    fonte_mortes = fonte.render(
            f'Mortes: {mortes}',
            True,
            (255, 255, 255)
        )
    superficie.blit(fonte_mortes,(20,70))
    
    # Carrosel da imagem de fundo
    # rel_x = fundoX % fundo.get_rect().width
    # superficie.blit(fundo,(rel_x - fundo.get_rect().width,0)) # cria background
    # if rel_x < 1280:
    #    superficie.blit(fundo,(rel_x,0))

    grupo_duno.draw(superficie)
    grupo_inimigos.draw(superficie)
    grupo_torradas.draw(superficie)

    grupo_duno.update()
    grupo_inimigos.update()
    grupo_torradas.update()
  

    #fundoX -= 0.3

    if perdeu:
        deu_ruim = fonte_perdeu.render(
            'Voce perdeu',
            True,
            (255, 255, 255)
        )
        superficie.blit(deu_ruim, (100, 200))
        display.update()
        pygame.time.delay(10000)


    round += 1
    display.update()
    
    





