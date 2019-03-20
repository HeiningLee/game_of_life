import pygame
from pygame.sprite import Sprite


class Cell(Sprite):
    # Initialize one cell, not posted on the grid yet. We'll do that in Cells.
    def __init__(self, gameset, screen, cellx, celly):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(cellx,
                                celly,
                                gameset.cellsize,
                                gameset.cellsize)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = gameset.cellcolor

    def draw_cell(self):
        # draw cell on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)





