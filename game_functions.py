import sys
import pygame
from cell import Cell


def check_events(gameset, gamestat, screen, atlas, cells):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                if gamestat.paused is True:
                    gamestat.paused = False
                    print("Game on")
                else:
                    gamestat.paused = True
                    print("Game paused")
            if event.key == pygame.K_c:
                gamestat.cellcounting = True
            if event.key == pygame.K_r:
                if gamestat.paused:
                    atlas.atlas_reset()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                gamestat.cellcounting = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gamestat.setcell = True
        elif event.type == pygame.MOUSEBUTTONUP:
            gamestat.setcell = False


def check_setcell(gameset, gamestat, screen, atlas, cells):
    if gamestat.paused:
        mousex, mousey = pygame.mouse.get_pos()
        mouse_nx = mousex // gameset.cellsize
        mouse_ny = mousey // gameset.cellsize

        if atlas.matrix[mouse_ny][mouse_nx] == 0:
           atlas.matrix[mouse_ny][mouse_nx] = 1

        create_cells(gameset, gamestat, screen, atlas, cells)
        draw_cells(gameset, screen, atlas, cells)


def create_cells(gameset, gamestat, screen, atlas, cells):
    # Creating cells according to atlas matrix
    cellcount = 0
    for i in range(atlas.ny):
        for j in range(atlas.nx):
            if atlas.matrix[i][j] == 1:
                cellx = j*gameset.cellsize
                celly = i*gameset.cellsize
                cell = Cell(gameset, screen, cellx, celly)
                cells.add(cell)
                cellcount += 1
    if gamestat.cellcounting:
        print(cellcount, 'cells')


def draw_cells(gameset, screen, atlas, cells):
    for cell in cells.copy():
        cell.draw_cell()
        cells.remove(cell)


def update_screen(gameset, screen, atlas, cells):
    screen.fill(gameset.bgcolor)
    draw_cells(gameset, screen, atlas, cells)
    pygame.display.flip()

