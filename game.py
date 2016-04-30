from board import Board
from player import Player
from functions import *
from pygame import mixer

# zmienne gry

WINDOW_SIZE_X = 650
WINDOW_SIZE_Y = 650
exit_game = False
menu_exit = False
amount_enemies = 0

pygame.init()
mixer.init()

# muzyka

pygame.mixer.music.load('music/song2.wav')
pygame.mixer.music.play(-1)

pygame.display.set_caption('Bomberman')
window = pygame.display.set_mode((WINDOW_SIZE_X, WINDOW_SIZE_Y))

# plansza

board = Board(WINDOW_SIZE_X, WINDOW_SIZE_Y)
board.generate()
board.show(window)
dark(window)

# menu

show_text_centered(window, WINDOW_SIZE_X, WINDOW_SIZE_Y-50, "BOMBERMAN", 80)
show_text_centered(window, WINDOW_SIZE_X, WINDOW_SIZE_Y+100, "[ E ] asy     [ M ] edium     [ H ] ard" , 25)
show_text_centered(window, WINDOW_SIZE_X, WINDOW_SIZE_Y+500, "2016 ADAM DYDERSKI" , 20)

pygame.display.update()

while not menu_exit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            menu_exit = True
            exit_game = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:
                amount_enemies = 6
                menu_exit = True
            if event.key == pygame.K_m:
                amount_enemies = 10
                menu_exit = True
            if event.key == pygame.K_h:
                amount_enemies = 14
                menu_exit = True

# gracz

player = Player()
player.start_position(board)

# wrogowie

generate_enemies(board, player, amount_enemies)

# zegar

clock = pygame.time.Clock()

# GRA

while not exit_game:

    board.show(window)
    show_character(window, player)
    show_bombs(window, board)
    show_enemies(window, board)

    for event in pygame.event.get():

        if event.type == pygame.QUIT: # wyjście z gry
            exit_game = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.move(board, (-1, 0))
                player.flip_left()

            if event.key == pygame.K_RIGHT:
                player.move(board, (1, 0))
                player.flip_right()

            if event.key == pygame.K_UP:
                player.move(board, (0, -1))

            if event.key == pygame.K_DOWN:
                player.move(board, (0, 1))

            if event.key == pygame.K_SPACE:
                add_bomb(board, player.x, player.y)

    enemies_flash(board)

    if end_game(player, board):
        bye(window, WINDOW_SIZE_X, WINDOW_SIZE_Y, "TRY AGAIN!")
        exit_game = True

    if win_game(board):
        bye(window, WINDOW_SIZE_X, WINDOW_SIZE_Y, "YOU WIN!")
        exit_game = True

    move_enemies(board, player)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
