import pygame
import game_functions as gf
from settings import Settings
from game_stat import GameStat
from atlas import Atlas
from pygame.sprite import Group


def run_game():
    # game settings
    cells = Group()
    gameset = Settings()
    gamestat = GameStat()
    atlas = Atlas(gameset)
    pygame.init()
    screen = pygame.display.set_mode((gameset.scr_width, gameset.scr_height))
    pygame.display.set_caption("Conway's Game of Life")

    # main loop. 2 steps only for test.
    evolvecount = 2
    while True:
        gf.check_events(gameset, gamestat, screen, atlas, cells)
        # when the mouse is pressed down, begin setcell
        if gamestat.setcell:
            gf.check_setcell(gameset, gamestat, screen, atlas, cells)
            print('matrix after cellset')
            print(atlas.matrix)
        # when game is on, atlas evolve itself.
        if not gamestat.paused:
            atlas.evolve()
            evolvecount -= 1

        # create cells according to atlas, and draw them.
        gf.create_cells(gameset, gamestat, screen, atlas, cells)
        gf.update_screen(gameset, screen, atlas, cells)


# run the game
run_game()

