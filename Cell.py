import pygame
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)


class Cell:

    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = BLACK
        self.width = width
        self.walls = [True, True, True, True]
        self.neighbors = []
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

    def find_neighbors(self, grid, rows, cols):
        topx = self.row - 1
        bottomx = self.row + 1
        lefty = self.col - 1
        righty = self.col + 1
        # top
        if not topx < 0:
            self.neighbors.append(grid[topx][self.col])
        # bottom
        if not bottomx > rows - 1:
            self.neighbors.append(grid[bottomx][self.col])
        # left
        if not lefty < 0:
            self.neighbors.append(grid[self.row][lefty])
        # right
        if not righty > cols - 1:
            self.neighbors.append(grid[self.row][righty])

    def next_move(self):
        if len(self.neighbors) > 0:
            return self.neighbors[random.randint(0, len(self.neighbors) - 1)]


    def visited_location(self, win):
        self.visited = True
        pygame.draw.rect(win, YELLOW, [self.x, self.y, self.width, self.width])

    def __lt__(self, other):
        return False