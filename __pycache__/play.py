import pygame, random, time, os
black = (0,0,0)
white = (255,255,255)
silver = (211,211,211)
pygame.display.init()
GameBoard = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
from grid import grid, Grid
from input import input
GameBoard.fill(silver)
grid()
Grid()
input()

if __name__ == '__main__':
    pygame.init()
    input()
    pygame.quit()
