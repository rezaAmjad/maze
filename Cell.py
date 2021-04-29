import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)


class Cell:

    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.walls = [True, True, True, True]
        self.visited = False

    def draw(self, win):

        # top
        if self.walls[0]:
            pygame.draw.line(win, self.color, (self.x, self.y), (self.x + self.width, self.y))
        # left
        if self.walls[1]:
            pygame.draw.line(win, self.color, (self.x, self.y), (self.x, self.y + self.width))
        # bottom
        if self.walls[2]:
            pygame.draw.line(win, self.color, (self.x, self.y + self.width),
                             (self.x + self.width, self.y + self.width))
        # right
        if self.walls[3]:
            pygame.draw.line(win, self.color, (self.x + self.width, self.y),
                             (self.x + self.width, self.y + self.width))

