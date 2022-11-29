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

pygame.init()

tamanho = 800, 600

superficie = display.set_mode(size=tamanho, display=0)

display.set_caption('Torradas espaciais')

fundo = scale(load('images/space.jpg'), tamanho)


class Dunofausto(Sprite):
    def __init__(self):
        super().__init__()

        self.image = load('images/dunofausto_small.png')
        self.rect = self.image.get_rect()

class Torrada(Sprite):
    def __init__(self):
        super().__init__()

        self.image = load('images/torrada_small.png')
        self.rect = self.image.get_rect()

class Virus(Sprite):
    def __init__(self):
        super().__init__()

        self.image = load('images/inimigo_1.png')
        self.rect = self.image.get_rect()


dunofausto = Dunofausto()

while True:
    # loop de eventos

    # Espaço do display
    superficie.blit(fundo,(0,0))

    display.update()