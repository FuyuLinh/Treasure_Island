import pygame


class Cell(object):
    rows = 0
    width = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def draw(self):
        pass



def drawGrid(width, rows, surface):
    sizeBtwn = width // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))
