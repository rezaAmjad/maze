import pygame
import math
from Cell import Cell
import tkinter as tk
from tkinter import *

# root = tk.Tk()
# root.title("Path finding")
# main_frame = tk.Frame(root, width=802, height=1002)
# stat_frame = tk.Frame(main_frame,width=802, height=1002 - 802)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Generator")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
w = 40
# if one '/' is used the following error would occur
# float' object cannot be interpreted as an integer


grid = []


visited = None

def make_grid():
    rows = math.floor(WINDOW_WIDTH // w)
    cols = math.floor(WINDOW_HEIGHT // w)
    for i in range(rows):
        for j in range(cols):
            c = Cell(i, j, w)
            grid.append(c)


def main():
    done = False
    make_grid()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for c in grid:
                c.draw(WIN)

        pygame.display.update()


if __name__ == "__main__":
    main()
