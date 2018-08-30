import pygame
from random import randint
import pygame
from random import randint
pygame.init()
black = (0,0,0)
white = (255,255,255)
silver = (211,211,211)
red = (255, 0, 0)
blue = (0, 0, 128)
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
    ship_row = random_row(board)
    ship_col = random_col(board)
    coord.append(ship_row)
    coord.append(ship_col)
    print(coord)
    while thing == 0:
        guess_row = float(input('Input Ship Row: '))
        guess.append(guess_row)
        guess_col = float(input('Input Ship Col: '))
        guess.append(guess_col)
        print(guess)
        if guess == coord:
            print('aye')
            thing = thing + 1
            guess = []
        else:
            print('nay')
            guess = []
            if guess_col == 0:
                print('0')
                if guess_row == 0:
                    print('0')
                    pygame.draw.rect(GameBoard, blue, [50, 50, 40, 40])
                    pygame.display.flip()
                else:
                    if guess_row == 1:
                        print('1')
                        pygame.draw.rect(GameBoard, blue, [50, 90, 40, 40])
                        pygame.display.flip()
                    else:
                        if guess_row == 2:
                            print('2')
                            pygame.draw.rect(GameBoard, blue, [50, 130, 40, 40])
                            pygame.display.flip()
                        else:
                            if guess_row == 3:
                                print('3')
                                pygame.draw.rect(GameBoard, blue, [50, 170, 40, 40])
                                pygame.display.flip()
                            else:
                                if guess_row == 4:
                                    print('4')
                                    pygame.draw.rect(GameBoard, blue, [50, 210, 40, 40])
                                    pygame.display.flip()
                                else:
                                    if guess_row == 5:
                                        print('5')
                                        pygame.draw.rect(GameBoard, blue, [50, 250, 40, 40])
                                        pygame.display.flip()
                                    else:
                                        if guess_row == 6:
                                            print('6')
                                            pygame.draw.rect(GameBoard, blue, [50, 290, 40, 40])
                                            pygame.display.flip()
                                        else:
                                            if guess_row == 7:
                                                print('7')
                                                pygame.draw.rect(GameBoard, blue, [50, 330, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 8:
                                                    print('8')
                                                    pygame.draw.rect(GameBoard, blue, [50, 370, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 9:
                                                        print('9')
                                                        pygame.draw.rect(GameBoard, blue, [50, 410, 40, 40])
                                                        pygame.display.flip()
            else:
                if guess_col == 1:
                    print('1')
                    if guess_row == 0:
                        print('0')
                        pygame.draw.rect(GameBoard, blue, [90, 50, 40, 40])
                        pygame.display.flip()
                    else:
                        if guess_row == 1:
                            print('1')
                            pygame.draw.rect(GameBoard, blue, [90, 90, 40, 40])
                            pygame.display.flip()
                        else:
                            if guess_row == 2:
                                print('2')
                                pygame.draw.rect(GameBoard, blue, [90, 130, 40, 40])
                                pygame.display.flip()
                            else:
                                if guess_row == 3:
                                    print('3')
                                    pygame.draw.rect(GameBoard, blue, [90, 170, 40, 40])
                                    pygame.display.flip()
                                else:
                                    if guess_row == 4:
                                        print('4')
                                        pygame.draw.rect(GameBoard, blue, [90, 210, 40, 40])
                                        pygame.display.flip()
                                    else:
                                        if guess_row == 5:
                                            print('5')
                                            pygame.draw.rect(GameBoard, blue, [90, 250, 40, 40])
                                            pygame.display.flip()
                                        else:
                                            if guess_row == 6:
                                                print('6')
                                                pygame.draw.rect(GameBoard, blue, [90, 290, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 7:
                                                    print('7')
                                                    pygame.draw.rect(GameBoard, blue, [90, 330, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 8:
                                                        print('8')
                                                        pygame.draw.rect(GameBoard, blue, [90, 370, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 9:
                                                            print('9')
                                                            pygame.draw.rect(GameBoard, blue, [50, 410, 40, 40])
                                                            pygame.display.flip()
                else:
                    if guess_col == 2:
                        print('2')
                        if guess_row == 0:
                            print('0')
                            pygame.draw.rect(GameBoard, blue, [130, 50, 40, 40])
                            pygame.display.flip()
                        else:
                            if guess_row == 1:
                                print('1')
                                pygame.draw.rect(GameBoard, blue, [130, 90, 40, 40])
                                pygame.display.flip()
                            else:
                                if guess_row == 2:
                                    print('2')
                                    pygame.draw.rect(GameBoard, blue, [130, 130, 40, 40])
                                    pygame.display.flip()
                                else:
                                    if guess_row == 3:
                                        print('3')
                                        pygame.draw.rect(GameBoard, blue, [130, 170, 40, 40])
                                        pygame.display.flip()
                                    else:
                                        if guess_row == 4:
                                            print('4')
                                            pygame.draw.rect(GameBoard, blue, [130, 210, 40, 40])
                                            pygame.display.flip()
                                        else:
                                            if guess_row == 5:
                                                print('5')
                                                pygame.draw.rect(GameBoard, blue, [130, 250, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 6:
                                                    print('6')
                                                    pygame.draw.rect(GameBoard, blue, [130, 290, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 7:
                                                        print('7')
                                                        pygame.draw.rect(GameBoard, blue, [130, 330, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 8:
                                                            print('8')
                                                            pygame.draw.rect(GameBoard, blue, [130, 370, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 9:
                                                                print('9')
                                                                pygame.draw.rect(GameBoard, blue, [130, 410, 40, 40])
                                                                pygame.display.flip()
                    else:
                        if guess_col == 3:
                            print('3')
                            if guess_row == 0:
                                print('0')
                                pygame.draw.rect(GameBoard, blue, [170, 50, 40, 40])
                                pygame.display.flip()
                            else:
                                if guess_row == 1:
                                    print('1')
                                    pygame.draw.rect(GameBoard, blue, [170, 90, 40, 40])
                                    pygame.display.flip()
                                else:
                                    if guess_row == 2:
                                        print('2')
                                        pygame.draw.rect(GameBoard, blue, [170, 130, 40, 40])
                                        pygame.display.flip()
                                    else:
                                        if guess_row == 3:
                                            print('3')
                                            pygame.draw.rect(GameBoard, blue, [170, 170, 40, 40])
                                            pygame.display.flip()
                                        else:
                                            if guess_row == 4:
                                                print('4')
                                                pygame.draw.rect(GameBoard, blue, [170, 210, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 5:
                                                    print('5')
                                                    pygame.draw.rect(GameBoard, blue, [170, 250, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 6:
                                                        print('6')
                                                        pygame.draw.rect(GameBoard, blue, [170, 290, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 7:
                                                            print('7')
                                                            pygame.draw.rect(GameBoard, blue, [170, 330, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 8:
                                                                print('8')
                                                                pygame.draw.rect(GameBoard, blue, [170, 370, 40, 40])
                                                                pygame.display.flip()
                                                            else:
                                                                if guess_row == 9:
                                                                    print('9')
                                                                    pygame.draw.rect(GameBoard, blue, [170, 410, 40, 40])
                                                                    pygame.display.flip()
                        else:
                            if guess_col == 4:
                                print('4')
                                if guess_row == 0:
                                    print('0')
                                    pygame.draw.rect(GameBoard, blue, [210, 50, 40, 40])
                                    pygame.display.flip()
                                else:
                                    if guess_row == 1:
                                        print('1')
                                        pygame.draw.rect(GameBoard, blue, [210, 90, 40, 40])
                                        pygame.display.flip()
                                    else:
                                        if guess_row == 2:
                                            print('2')
                                            pygame.draw.rect(GameBoard, blue, [210, 130, 40, 40])
                                            pygame.display.flip()
                                        else:
                                            if guess_row == 3:
                                                print('3')
                                                pygame.draw.rect(GameBoard, blue, [210, 170, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 4:
                                                    print('4')
                                                    pygame.draw.rect(GameBoard, blue, [210, 210, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 5:
                                                        print('5')
                                                        pygame.draw.rect(GameBoard, blue, [210, 250, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 6:
                                                            print('6')
                                                            pygame.draw.rect(GameBoard, blue, [210, 290, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 7:
                                                                print('7')
                                                                pygame.draw.rect(GameBoard, blue, [210, 330, 40, 40])
                                                                pygame.display.flip()
                                                            else:
                                                                if guess_row == 8:
                                                                    print('8')
                                                                    pygame.draw.rect(GameBoard, blue, [210, 370, 40, 40])
                                                                    pygame.display.flip()
                                                                else:
                                                                    if guess_row == 9:
                                                                        print('9')
                                                                        pygame.draw.rect(GameBoard, blue, [210, 410, 40, 40])
                                                                        pygame.display.flip()
                            else:
                                if guess_col == 5:
                                    print('5')
                                    if guess_row == 0:
                                        print('0')
                                        pygame.draw.rect(GameBoard, blue, [250, 50, 40, 40])
                                        pygame.display.flip()
                                    else:
                                        if guess_row == 1:
                                            print('1')
                                            pygame.draw.rect(GameBoard, blue, [250, 90, 40, 40])
                                            pygame.display.flip()
                                        else:
                                            if guess_row == 2:
                                                print('2')
                                                pygame.draw.rect(GameBoard, blue, [250, 130, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 3:
                                                    print('3')
                                                    pygame.draw.rect(GameBoard, blue, [250, 170, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 4:
                                                        print('4')
                                                        pygame.draw.rect(GameBoard, blue, [250, 210, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 5:
                                                            print('5')
                                                            pygame.draw.rect(GameBoard, blue, [250, 250, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 6:
                                                                print('6')
                                                                pygame.draw.rect(GameBoard, blue, [250, 290, 40, 40])
                                                                pygame.display.flip()
                                                            else:
                                                                if guess_row == 7:
                                                                    print('7')
                                                                    pygame.draw.rect(GameBoard, blue, [250, 330, 40, 40])
                                                                    pygame.display.flip()
                                                                else:
                                                                    if guess_row == 8:
                                                                        print('8')
                                                                        pygame.draw.rect(GameBoard, blue, [250, 370, 40, 40])
                                                                        pygame.display.flip()
                                                                    else:
                                                                        if guess_row == 9:
                                                                            print('9')
                                                                            pygame.draw.rect(GameBoard, blue, [250, 410, 40, 40])
                                                                            pygame.display.flip()
                                else:
                                    if guess_col == 6:
                                        print('6')
                                        if guess_row == 0:
                                            print('0')
                                            pygame.draw.rect(GameBoard, blue, [290, 50, 40, 40])
                                            pygame.display.flip()
                                        else:
                                            if guess_row == 1:
                                                print('1')
                                                pygame.draw.rect(GameBoard, blue, [290, 90, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 2:
                                                    print('2')
                                                    pygame.draw.rect(GameBoard, blue, [290, 130, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 3:
                                                        print('3')
                                                        pygame.draw.rect(GameBoard, blue, [290, 170, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 4:
                                                            print('4')
                                                            pygame.draw.rect(GameBoard, blue, [290, 210, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 5:
                                                                print('5')
                                                                pygame.draw.rect(GameBoard, blue, [290, 250, 40, 40])
                                                                pygame.display.flip()
                                                            else:
                                                                if guess_row == 6:
                                                                    print('6')
                                                                    pygame.draw.rect(GameBoard, blue, [290, 290, 40, 40])
                                                                    pygame.display.flip()
                                                                else:
                                                                    if guess_row == 7:
                                                                        print('7')
                                                                        pygame.draw.rect(GameBoard, blue, [290, 330, 40, 40])
                                                                        pygame.display.flip()
                                                                    else:
                                                                        if guess_row == 8:
                                                                            print('8')
                                                                            pygame.draw.rect(GameBoard, blue, [290, 370, 40, 40])
                                                                            pygame.display.flip()
                                                                        else:
                                                                            if guess_row == 9:
                                                                                print('9')
                                                                                pygame.draw.rect(GameBoard, blue, [290, 410, 40, 40])
                                                                                pygame.display.flip()
                                    else:
                                        if guess_col == 7:
                                            print('7')
                                            if guess_row == 0:
                                                print('0')
                                                pygame.draw.rect(GameBoard, blue, [330, 50, 40, 40])
                                                pygame.display.flip()
                                            else:
                                                if guess_row == 1:
                                                    print('1')
                                                    pygame.draw.rect(GameBoard, blue, [330, 90, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 2:
                                                        print('2')
                                                        pygame.draw.rect(GameBoard, blue, [330, 130, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 3:
                                                            print('3')
                                                            pygame.draw.rect(GameBoard, blue, [330, 170, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 4:
                                                                print('4')
                                                                pygame.draw.rect(GameBoard, blue, [330, 210, 40, 40])
                                                                pygame.display.flip()
                                                            else:
                                                                if guess_row == 5:
                                                                    print('5')
                                                                    pygame.draw.rect(GameBoard, blue, [330, 250, 40, 40])
                                                                    pygame.display.flip()
                                                                else:
                                                                    if guess_row == 6:
                                                                        print('6')
                                                                        pygame.draw.rect(GameBoard, blue, [330, 290, 40, 40])
                                                                        pygame.display.flip()
                                                                    else:
                                                                        if guess_row == 7:
                                                                            print('7')
                                                                            pygame.draw.rect(GameBoard, blue, [330, 330, 40, 40])
                                                                            pygame.display.flip()
                                                                        else:
                                                                            if guess_row == 8:
                                                                                print('8')
                                                                                pygame.draw.rect(GameBoard, blue, [330, 370, 40, 40])
                                                                                pygame.display.flip()
                                                                            else:
                                                                                if guess_row == 9:
                                                                                    print('9')
                                                                                    pygame.draw.rect(GameBoard, blue, [330, 410, 40, 40])
                                                                                    pygame.display.flip()
                                        else:
                                            if guess_col == 8:
                                                print('8')
                                                if guess_row == 0:
                                                    print('0')
                                                    pygame.draw.rect(GameBoard, blue, [370, 50, 40, 40])
                                                    pygame.display.flip()
                                                else:
                                                    if guess_row == 1:
                                                        print('1')
                                                        pygame.draw.rect(GameBoard, blue, [370, 90, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 2:
                                                            print('2')
                                                            pygame.draw.rect(GameBoard, blue, [370, 130, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 3:
                                                                print('3')
                                                                pygame.draw.rect(GameBoard, blue, [370, 170, 40, 40])
                                                                pygame.display.flip()
                                                            else:
                                                                if guess_row == 4:
                                                                    print('4')
                                                                    pygame.draw.rect(GameBoard, blue, [370, 210, 40, 40])
                                                                    pygame.display.flip()
                                                                else:
                                                                    if guess_row == 5:
                                                                        print('5')
                                                                        pygame.draw.rect(GameBoard, blue, [370, 250, 40, 40])
                                                                        pygame.display.flip()
                                                                    else:
                                                                        if guess_row == 6:
                                                                            print('6')
                                                                            pygame.draw.rect(GameBoard, blue, [370, 290, 40, 40])
                                                                            pygame.display.flip()
                                                                        else:
                                                                            if guess_row == 7:
                                                                                print('7')
                                                                                pygame.draw.rect(GameBoard, blue, [370, 330, 40, 40])
                                                                                pygame.display.flip()
                                                                            else:
                                                                                if guess_row == 8:
                                                                                    print('8')
                                                                                    pygame.draw.rect(GameBoard, blue, [370, 370, 40, 40])
                                                                                    pygame.display.flip()
                                                                                else:
                                                                                    if guess_row == 9:
                                                                                        print('9')
                                                                                        pygame.draw.rect(GameBoard, blue, [370, 410, 40, 40])
                                                                                        pygame.display.flip()
                                            else:
                                                if guess_col == 9:
                                                    print('9')
                                                    if guess_row == 0:
                                                        print('0')
                                                        pygame.draw.rect(GameBoard, blue, [410, 50, 40, 40])
                                                        pygame.display.flip()
                                                    else:
                                                        if guess_row == 1:
                                                            print('1')
                                                            pygame.draw.rect(GameBoard, blue, [410, 90, 40, 40])
                                                            pygame.display.flip()
                                                        else:
                                                            if guess_row == 2:
                                                                print('2')
                                                                pygame.draw.rect(GameBoard, blue, [410, 130, 40, 40])
                                                                pygame.display.flip()
                                                            else:
                                                                if guess_row == 3:
                                                                    print('3')
                                                                    pygame.draw.rect(GameBoard, blue, [410, 170, 40, 40])
                                                                    pygame.display.flip()
                                                                else:
                                                                    if guess_row == 4:
                                                                        print('4')
                                                                        pygame.draw.rect(GameBoard, blue, [410, 210, 40, 40])
                                                                        pygame.display.flip()
                                                                    else:
                                                                        if guess_row == 5:
                                                                            print('5')
                                                                            pygame.draw.rect(GameBoard, blue, [410, 250, 40, 40])
                                                                            pygame.display.flip()
                                                                        else:
                                                                            if guess_row == 6:
                                                                                print('6')
                                                                                pygame.draw.rect(GameBoard, blue, [410, 290, 40, 40])
                                                                                pygame.display.flip()
                                                                            else:
                                                                                if guess_row == 7:
                                                                                    print('7')
                                                                                    pygame.draw.rect(GameBoard, blue, [410, 330, 40, 40])
                                                                                    pygame.display.flip()
                                                                                else:
                                                                                    if guess_row == 8:
                                                                                        print('8')
                                                                                        pygame.draw.rect(GameBoard, blue, [410, 370, 40,40])
                                                                                        pygame.display.flip()
                                                                                    else:
                                                                                        if guess_row == 9:
                                                                                            print('9')
                                                                                            pygame.draw.rect(GameBoard, blue, [410, 410, 40, 40])
                                                                                            pygame.display.flip()