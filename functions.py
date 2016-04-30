import random
from time import gmtime, strftime, sleep
from bomb import Bomb
from enemy import Enemy
import pygame


# pokaż


def show_character(window, character):
    window.blit(character.img, (character.x, character.y))


def show_enemies(window, board):

    for enemy in board.enemies:
        show_character(window, enemy)


def show_bombs(window, board):

    for bomb in board.bombs:

        bomb.check_bomb()

        if bomb.exist == 1:
            window.blit(bomb.bomb_img, (bomb.x, bomb.y))
        else:

            if not bomb.end_flash():

                for x, y in bomb.flashes:

                    if (x, y) not in board.walls:
                        window.blit(bomb.flash_img, (x, y))

                    if (x, y) in board.boxes:
                        board.boxes.remove((x, y))
            else:
                board.bombs.remove(bomb)

# ruchy


def move_enemies(board, player):

    for enemy in board.enemies:
        enemy.move(board, player)

# sprawdzanie


def safe_places_to_move(board,player, x, y):

    moves = [] # lista możliwych ruchów

    for i, j in [(x - 50, y), (x + 50, y), (x, y - 50), (x, y + 50)]: # góra, dół, prawo, lewo

        if (i, j) not in board.boxes and (i, j) not in board.walls and not board.out_of_board(i, j) \
                and not enemy_collision(board, i, j) and not (i, j) == (player.x, player.y) and bomb_free_place(board, i, j) \
                and (i, j) not in board.shelters:
            moves.append((i, j))

    return moves


def bomb_free_place(board, x, y):

    for bomb in board.bombs:
        if (x, y) in bomb.flashes or (x, y) == (bomb.x, bomb.y):
            return False

    return True


def place_for_bomb(board, x, y):

    for i, j in [(x - 50, y), (x + 50, y), (x, y - 50), (x, y + 50)]:
        if (i, j) in board.shelters:
            return False

    for enemy in board.enemies:

        if not (x, y) == (enemy.x, enemy.y): # wszyscy poza mną

            if (enemy.x, enemy.y) in [(x - 50, y), (x + 50, y), (x, y - 50), (x, y + 50)]:
                return False

    return True


def enemy_collision(board, x, y):

    for enemy in board.enemies:
        if (enemy.x, enemy.y) == (x, y):
            return True

    return False


def add_bomb(board, x, y):
    now = time_now()

    new_bomb = Bomb(x, y, 2, now)
    board.bombs.append(new_bomb)


def time_now():
    return int(strftime("%S", gmtime())) # sekundy


def generate_enemies(board, player, n):

    for _ in range(n):
        enemy = Enemy()
        enemy.start_position(board, player)
        board.enemies.append(enemy)


def enemies_flash(board):

    for bomb in board.bombs:
        for enemy in board.enemies:

            if bomb.exist == 0 and (enemy.x,enemy.y) in bomb.flashes:
                board.enemies.remove(enemy)

# wygrany / przegrany


def end_game(player, board):

    for bomb in board.bombs:
        if bomb.exist == 0 and (player.x, player.y) in bomb.flashes:
            return True

    return False


def win_game(board):
    return len(board.enemies) == 0


# napis


def dark(window):
    window.fill((100, 100, 100, 128), None, pygame.BLEND_RGBA_MULT)


def show_text_centered(window, x, y, text, size=70):

    font = pygame.font.Font("font/font.ttf", size)
    label = font.render(text, 1, (255, 255, 255))
    window.blit(label, ((x-label.get_rect().width)/2, (y-label.get_rect().height)/2))


# wyjscie


def bye(window, x, y, text):

    dark(window)
    show_text_centered(window, x, y, text, 70)
    pygame.display.update()
    pygame.mixer.music.fadeout(2000)
    sleep(2)





