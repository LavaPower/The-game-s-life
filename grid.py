from random import randint
import pygame as pg


class Grid:
    m_line_wth = 2
    m_square_wth = 10
    m_square_hght = 10
    m_grid = [[0 for column in range(67)] for row in range(50)]

    def __init__(self, _win):
        for row in range(50):
            for column in range(67):
                pg.draw.rect(_win, (255, 255, 255),
                             [(self.getLine_wth() + self.getSquare_wth()) * column + self.getLine_wth(),
                              (self.getLine_wth() + self.getSquare_hght()) * row + self.getLine_wth(),
                              self.getSquare_wth(), self.getSquare_hght()])

    @classmethod
    def select_cell(cls):
        pos = pg.mouse.get_pos()
        column = pos[0] // (Grid.m_square_wth + Grid.m_line_wth)
        row = pos[1] // (Grid.m_square_hght + Grid.m_line_wth)
        cls.m_grid[row][column] = 1
        print("Click ", pos, "Grid coordinates: ", row, column)

    @classmethod
    def generate_life(cls, _win):
        random_cell_r, random_cell_c = randint(0, 67 * (Grid.m_square_wth + Grid.m_line_wth)) // (Grid.m_square_wth + Grid.m_line_wth), randint(0, 50 * (Grid.m_square_wth + Grid.m_line_wth)) // (Grid.m_square_hght + Grid.m_line_wth)
        #print(f"Touch ({random_cell_c, random_cell_r})")
        pg.draw.rect(_win, (0, 0, 0), (pg.Rect(random_cell_r*cls.getSquare_wth()+cls.getLine_wth()*random_cell_r, random_cell_c*cls.getSquare_hght()+cls.getLine_wth()*random_cell_c, cls.getSquare_wth()*1.4, cls.getSquare_hght()*1.4)))

    @classmethod
    def getLine_wth(cls):
        return cls.m_line_wth

    @classmethod
    def getSquare_wth(cls):
        return cls.m_square_wth

    @classmethod
    def getSquare_hght(cls):
        return cls.m_square_hght

    @classmethod
    def setLine_wth(cls, value):
        cls.m_line_wth = value

    @classmethod
    def setSquare_wth(cls, value):
        cls.m_square_wth = value

    @classmethod
    def setSquare_hght(cls, value):
        cls.m_square_hght = value

