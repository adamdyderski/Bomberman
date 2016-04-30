import pygame
import functions
import random


class Enemy:

    def __init__(self):

        self.x = 0
        self.y = 0

        # tekstury

        self.right = 1
        self.img = pygame.image.load('img/enemy_r.png')

        # czas

        self.move_time = (functions.time_now() + 1) % 60

        # kryjówka

        self.shelter = (-1, -1)

    def start_position(self, board, player):

        while True:
            x = random.randrange(0, board.size_x, board.cube_size)
            y = random.randrange(0, board.size_y, board.cube_size)

            free_space = 0

            for i, j in [(x - 50, y), (x + 50, y), (x, y - 50), (x, y + 50)]:
                if (i, j) not in board.walls and (i, j) not in board.boxes and not board.out_of_board(i, j):
                    free_space += 1

            if (x, y) not in board.walls and (x, y) not in board.boxes and free_space >= 2 \
                    and not (x, y) == (player.x, player.y) and not functions.enemy_collision(board, x, y):
                break

        self.x = x
        self.y = y

    def time_to_move(self):

        now = functions.time_now()

        if now == self.move_time:
            self.move_time = (now + 1) % 60
            return True
        else:
            return False
        
    def move(self, board, player):

        if self.time_to_move():

            moves = functions.safe_places_to_move(board, player, self.x, self.y)

            if not self.shelter == (-1, -1):

                if (not functions.bomb_free_place(board, *self.shelter) or self.shelter == (player.x, player.y)) and len(moves) > 0:
                    board.shelters.remove(self.shelter)
                    self.shelter = (-1, -1)
                    new_x, new_y = random.choice(moves)  # nowe schronienie

                else:
                    new_x, new_y = self.shelter
                    board.shelters.remove(self.shelter)
                    self.shelter = (-1, -1)

                if self.x < new_x:
                    self.flip_right()
                else:
                    self.flip_left()

                self.x, self.y = new_x, new_y

            elif len(moves) > 0:

                new_x, new_y = random.choice(moves)

                # bomba

                run_away = functions.safe_places_to_move(board, player, new_x, new_y)

                if functions.place_for_bomb(board, self.x, self.y) and len(run_away) > 0:
                    functions.add_bomb(board, self.x, self.y)
                    self.shelter = random.choice(run_away)
                    board.shelters.append(self.shelter)

                if self.x < new_x:
                    self.flip_right()
                else:
                    self.flip_left()

                self.x, self.y = new_x, new_y

    def flip_right(self):

        if self.right == 0:
            self.img = pygame.image.load('img/enemy_r.png')
            self.right = 1

    def flip_left(self):

        if self.right == 1:
            self.img = pygame.image.load('img/enemy_l.png')
            self.right = 0





