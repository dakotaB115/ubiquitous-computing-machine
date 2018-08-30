import pygame
from random import randint
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ============================= // ==================================
# *******************************************************************
# *******************************************************************
# ===================================================================
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ======================= Game Grid =================================
black = (0,0,0)
white = (255,255,255)
silver = (211,211,211)
GameBoard = pygame.display.set_mode((700, 600))
def Grid():
    board = []
    coord = ''
    for x in range(0,10):
        board.append(["O"] * 10)
    def print_board(board):
        # insert 1
        for row in board:
            # insert 2
            print(" ".join(row))
    print_board(board)

    def random_row(board):
        # insert 1
        return randint(0, len(board) - 1)

    def random_col(board):
        # insert 1
        return randint(1, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    coord.append(ship_row)
    coord.append(ship_col)
    print(coord)
def grid():
    for h in range(1, 101):
        submarine = pygame.image.load("images/submarine.png").convert()  # 8
        cruiser = pygame.image.load("images/cruiser.png").convert()  # 9
        battleship = pygame.image.load("images/battleship.png").convert()  # 10
        destroyer = pygame.image.load("images/destroyer.png").convert()  # 11
        aircraft_carrier = pygame.image.load("images/aircraft_carrier.png").convert()  # 12
        two = pygame.image.load("images/2x1.png").convert()  # 13
        three = pygame.image.load("images/3x1.png").convert()  # 14
        four = pygame.image.load("images/4x1.png").convert()  # 15
        five = pygame.image.load("images/5x1.png").convert()  # 16
        background = pygame.image.load("images/10x10.png").convert()
        GameBoard.blit(background, [10, 10])
        #GameBoard.blit(submarine, [460, 180])
        #GameBoard.blit(cruiser, [460, 270])
        #GameBoard.blit(battleship, [460, 90])
        #GameBoard.blit(destroyer, [460, 360])
        #GameBoard.blit(aircraft_carrier, [460, 0])
        #GameBoard.blit(two, [460, 410])
        #GameBoard.blit(three, [460, 230])
        #GameBoard.blit(three, [460, 320])
        #GameBoard.blit(four, [460, 140])
        #GameBoard.blit(five, [460, 50])
        x = 50  # spacing on x direction
        y = 50  # spacing on y direction
        for i in range(11):
            pygame.draw.line(GameBoard, black, (40, y), (450, y))
            pygame.draw.line(GameBoard, black, (x, 40), (x, 450))
            y += 40
            x += 40
            pygame.display.update()

        # ===================================================================
        # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ============================ Patrol Ship ==========================

        # ===================================================================
        # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # =========================== Cruiser ===============================

        # ===================================================================
        # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ========================== Destroyer ==============================

        # ===================================================================
        # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ======================= BattleShip ================================

        # ===================================================================
        # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ===================== Aircraft Carrier ============================

        # ===================================================================