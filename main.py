import pygame
import math
from Cell import Cell


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
BLACK = (0, 0, 0)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WIN.fill(WHITE)
pygame.display.set_caption("Maze Generator")


w = 40
# if one '/' is used the following error would occur
# float' object cannot be interpreted as an integer
rows = math.floor(WINDOW_WIDTH // w)
cols = math.floor(WINDOW_HEIGHT // w)


visited_list = []


def make_grid():
    g = []

    for i in range(rows):
        g.append([])
        for j in range(cols):
            c = Cell(i, j, w)
            g[i].append(c)
    return g


def main():
    done = False
    grid = make_grid()

    fc = grid[0][0]
    print(fc.row , fc.col)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for i in range(cols):
                for c in grid[i]:
                   c.draw(WIN)

        pygame.display.update()
        fc.visited_location(WIN)
        fc.find_neighbors(grid, rows, cols)
        next_move = fc.next_move()
        fc = next_move
        fc.visited_location(WIN)
        fc.find_neighbors(grid, rows, cols)


if __name__ == "__main__":
    main()
