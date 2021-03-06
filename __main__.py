import time
import copy
from random import randint

import pygame as pg
import os

os.environ['SDL_VIDEO_CENTERED'] = str(1)


def draw(_line_wth, _square_wth):
    for row in range(50):
        for column in range(67):
            pg.draw.rect(win, (52, 73, 94),
                         [(_line_wth + _square_wth) * column + _line_wth,
                          (_line_wth + _square_wth) * row + _line_wth,
                          _square_wth, _square_wth])
            cells_table[row, column] = False


def select_cells():
    pos = pg.mouse.get_pos()
    column = pos[0] // (square_wth + line_wth)
    row = pos[1] // (square_wth + line_wth)
    cells_table[row, column] = not cells_table[row, column]

    pg.draw.rect(win, (42, 204, 113) if cells_table[row, column] else (52, 73, 94), (
        pg.Rect(column * square_wth + line_wth * (column + 1),
                row * square_wth + line_wth * (row + 1), square_wth,
                square_wth)))


def life_state(_cells_table):
    new_cells_table = copy.deepcopy(_cells_table)
    for row in range(1, 49):
        for column in range(1, 66):
            neighbours_count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if _cells_table[row + x, column + y] and (x is not 0 or y is not 0):
                        neighbours_count += 1

            new_cells_table[row, column] = True if (not _cells_table[row, column] and neighbours_count == 3) or (_cells_table[row, column] and (neighbours_count == 2 or neighbours_count == 3)) else False
    return new_cells_table


def square_colors(_cells_table):
    [pg.draw.rect(win, (42, 204, 113) if cells_table[row, column] else (52, 73, 94) , (
        pg.Rect(column * square_wth + line_wth * (column + 1),
            row * square_wth + line_wth * (row + 1), square_wth,
            square_wth))) for column in range(1, 66) for row in range(1, 49)]
    time.sleep(0.3)


pg.init()
win = pg.display.set_mode((1000, 700))
pg.display.set_caption("The game's life")
pg.display.set_icon(pg.image.load("icone.png"))
win.blit(pg.image.load("background.png").convert(), (0, 0))
count_font = pg.font.Font("Custom_Font_Pixel.ttf", 50)
count = 0
count_display = count_font.render(str(count), 0, (42, 204, 113))
win.blit(count_display, (370, 635))

cells_table, line_wth, square_wth = {}, 2, 10
draw(line_wth, square_wth)

while 1:
    pg.display.update()
    for _ in pg.event.get():
        key = pg.key.get_pressed()
        if key[pg.K_ESCAPE] or _.type == pg.QUIT:
            pg.quit()
            os.sys.exit(0)
        elif key[pg.K_p]:
            while 1:
                cells_table = life_state(cells_table)
                square_colors(cells_table)
                pg.display.update()
                count += 1
                pg.draw.rect(win, (27, 27, 27), (pg.Rect(370, 635, 100, 400)))

                count_display = count_font.render(str(count), 0, (42, 204, 113))
                win.blit(count_display, (370, 635))

        elif _.type == pg.MOUSEBUTTONDOWN:
            select_cells()