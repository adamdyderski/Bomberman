import pygame
from time import gmtime, strftime


class Bomb:

    def __init__(self, x, y, delay, now):

        self.x = x
        self.y = y

        # tekstury

        self.bomb_img = pygame.image.load('img/bomb.png')
        self.bomb_red_img = pygame.image.load('img/bombred.png')
        self.flash_img = pygame.image.load('img/pow.png')

        # wybuch

        self.explosion = (now+delay) % 60
        self.exist = 1

        # błyski

        self.flashes = [(x, y), (x-50, y), (x+50, y), (x, y-50), (x, y+50)]
        self.flash_end = (self.explosion + delay - 1) % 60

    def check_bomb(self):
        now = int(strftime("%S", gmtime()))

        if now == self.explosion-1:
            self.bomb_img = self.bomb_red_img # czerwona bomba
        elif now == self.explosion:
            self.exist = 0

    def end_flash(self):
        now = int(strftime("%S", gmtime()))

        if now == self.flash_end:
            return True
        else:
            return False

