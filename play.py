import pygame
from random import randint
pygame.init()
black = (0,0,0)
white = (255,255,255)
silver = (211,211,211)
pygame.display.init()
GameBoard = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
GameBoard.fill(silver)
done=False
from grid import Grid
def grid():
    for h in range(1, 101):
        background = pygame.image.load("images/10x10.png").convert()
        GameBoard.blit(background, [10, 10])
        x = 50  # spacing on x direction
        y = 50  # spacing on y direction
        for i in range(11):
            pygame.draw.line(GameBoard, black, (40, y), (450, y))
            pygame.draw.line(GameBoard, black, (x, 40), (x, 450))
            y += 40
            x += 40
            pygame.display.update()
grid()
Grid()
while(done==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
quit()
