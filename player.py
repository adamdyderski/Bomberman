import pygame
import functions
import random


class Player:

    def __init__(self):

        self.x = 0
        self.y = 0

        # tekstyury

        self.right = 1
        self.img = pygame.image.load('img/player_r.png')

    def start_position(self, board):

        while True:
            x = random.randrange(0, board.size_x, board.cube_size)
            y = random.randrange(0, board.size_y, board.cube_size)

            free_space = 0

            for i, j in [(x-50, y), (x+50, y), (x, y-50), (x, y+50)]:
                if (i, j) not in board.walls and (i, j) not in board.boxes and not board.out_of_board(i, j):
                    free_space += 1

            if (x, y) not in board.walls and (x, y) not in board.boxes and free_space >= 3:
                break

        self.x = x
        self.y = y

    def move(self, board, direction):

        # x i y : 1,0,-1
        x, y = direction

        new_x = self.x + 50 * x
        new_y = self.y + 50 * y

        if (new_x, new_y) not in board.boxes and (new_x, new_y) not in board.walls \
                and not board.out_of_board(new_x, new_y) and not functions.enemy_collision(board, new_x, new_y):
            self.x = new_x
            self.y = new_y

    def flip_right(self):

        if self.right == 0:
            self.img = pygame.image.load('img/player_r.png')
            self.right = 1

    def flip_left(self):

        if self.right == 1:
            self.img = pygame.image.load('img/player_l.png')
            self.right = 0

