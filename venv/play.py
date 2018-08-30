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
def Grid():
    thing = 0
    coord = []
    board = []
    guess = []
    for x in range(0,10):
        board.append(["O"] * 10)
    def print_board(board):
        for row in board:
            print(" ".join(row))
    print_board(board)

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(1, len(board[0]) - 1)
    #here is part is where it appends to coord
    ship_row = random_row(board)
    ship_col = random_col(board)
    coord.append(ship_row)
    coord.append(ship_col)
    print(coord)
    if thing == 0:
        number = float(input('Input Ship Row: '))
        guess.append(number)
        number1 = float(input('Input Ship Col: '))
        guess.append(number1)
        print(guess)
        if guess == coord:
            print('aye')
            thing = thing + 1
            guess = []
        else:
            print('nay')
            guess = []
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
