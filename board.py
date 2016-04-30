import pygame
import random

class Board:

    def __init__(self, x, y):

        # wielkość okna/planszy

        self.size_x = x
        self.size_y = y

        self.cube_size = 50

        # tekstury

        self.bg_img = pygame.image.load('img/bg.jpg')
        self.wall_img = pygame.image.load('img/wall.jpg')
        self.box_img = pygame.image.load('img/box.jpg')

        #
        self.reserved_img = pygame.image.load('img/bg.jpg')

        # wspolrzedne

        self.walls = []
        self.boxes = []
        self.shelters = []

        # listy obiektów

        self.bombs = []
        self.enemies = []

    def generate(self):

        i, j = 0, 0

        # ściany

        for x in range(0, self.size_x, self.cube_size):
            for y in range(0, self.size_y, self.cube_size):
                if i % 2 == 0 and j % 2 == 0:
                    self.walls.append((x, y))
                j += 1
            i += 1

        # skrzynki

        for _ in range(60):

            x, y = 0, 0

            while (x, y) in self.walls or (x, y) in self.boxes:
                x = random.randrange(0, self.size_x, self.cube_size)
                y = random.randrange(0, self.size_y, self.cube_size)

            self.boxes.append((x, y))

    def show(self, window):

        for x in range(0, self.size_x, self.cube_size):
            for y in range(0, self.size_y, self.cube_size):

                if (x, y) in self.boxes:
                    window.blit(self.box_img, (x, y))
                elif (x, y) in self.walls:
                    window.blit(self.wall_img, (x, y))
                elif (x, y) in self.shelters:
                    window.blit(self.reserved_img, (x, y))
                else:
                    window.blit(self.bg_img, (x, y))

    def out_of_board(self, x, y):

        if 0 <= x < self.size_x and 0 <= y < self.size_y:
            return False
        else:
            return True


