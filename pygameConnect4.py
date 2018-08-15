import pygame
import sys
import time

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
EMPTY = (211, 211, 211)
FRAME_COLOR = (255, 255, 0)
SCREEN_WIDTH = 610
SCREEN_HEIGHT = 650
CIRCLE_RADIUS = 35
BARRIER = 15
FONT_SIZE = 25
NUM_IN_A_ROW = 4
BLANK = ' '
OCCUPIED = 'X'
MESSAGE_FONT = pygame.font.SysFont("comicsansms", FONT_SIZE)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def welcome():
    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    waiting = False
        SCREEN.fill(BLACK)
        pause = MESSAGE_FONT.render("WELCOME TO CONNECT 4", True, WHITE)
        SCREEN.blit(pause, [175, 275])
        pause = MESSAGE_FONT.render("PRESS SPACEBAR TO START", True, WHITE)
        SCREEN.blit(pause, [200, 325])
        pygame.display.update()

def showMenu():
    while True:
        SCREEN.fill(BLACK)
        choice = MESSAGE_FONT.render("CONNECT 4! TO PLAY AGAIN, PRESS SPACEBAR. TO QUIT, PRESS 'Q'", True, WHITE)
        SCREEN.blit(choice, [25, 300])
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return True
                elif e.key == pygame.K_q:
                    return False

def moveCount(totalMoves, MAX_MOVES):
    pygame.draw.rect(SCREEN, BLACK, (0, 620, SCREEN_WIDTH, 20))
    moves = MESSAGE_FONT.render("MOVES REMAINING UNTIL CAT GAME: " + str(MAX_MOVES - totalMoves), True, WHITE)
    SCREEN.blit(moves, [255, 620])
    pygame.display.update()

def playerPrompt(playerList):
    pygame.draw.rect(SCREEN, BLACK, (0, 570, SCREEN_WIDTH, 20))
    prompt = MESSAGE_FONT.render(playerList[0][0] + ", PLACE YOUR CHIP IN A COLUMN. TO QUIT, PRESS '0'", True, WHITE)
    SCREEN.blit(prompt, [60, 570])
    pygame.display.update()
    

def setGrid():
    grid = []

    pygame.draw.rect(SCREEN, BLACK, (0, 525, SCREEN_WIDTH, 125))
    choice = MESSAGE_FONT.render("1", True, WHITE)
    SCREEN.blit(choice, [50, 535])
    for col in range(1, 7):
        choice = MESSAGE_FONT.render(str(col + 1), True, WHITE)
        SCREEN.blit(choice, [50 + (col * ((CIRCLE_RADIUS*2) + BARRIER)), 535])
    pygame.display.update()

    for y in range(BARRIER + CIRCLE_RADIUS, 476, (CIRCLE_RADIUS*2) + BARRIER):
        for x in range(BARRIER + CIRCLE_RADIUS, 561, (CIRCLE_RADIUS*2) + BARRIER):
            pygame.draw.circle(SCREEN, EMPTY, (x, y), CIRCLE_RADIUS)
            grid.append((x, y))

    return grid

def getPlayerName():
    name = ""
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return name
                elif pygame.key.name(e.key) == "backspace":
                    name = name[:-1]
                elif len(pygame.key.name(e.key)) == 1:
                    name += pygame.key.name(e.key).upper()
        SCREEN.fill(BLACK)
        pause = MESSAGE_FONT.render("ENTER YOUR NAME BELOW!", True, WHITE)
        SCREEN.blit(pause, [175, 275])
        pause = MESSAGE_FONT.render("NAME:", True, WHITE)
        SCREEN.blit(pause, [140, 325])
        pause = MESSAGE_FONT.render(name, True, WHITE)
        pygame.draw.rect(SCREEN, BLACK, (200, 325, SCREEN_WIDTH, 20))
        SCREEN.blit(pause, [200, 325])
        pygame.display.update()

def switchPlayers(playerList):
    playerList[0], playerList[1] = playerList[1], playerList[0]

def checkForWinner(grid, x, y, color):
    # checks vertical
    count = 0
    for char in range(NUM_OF_ROWS):
        if grid[char][x] == color:
            count += 1
            if count == NUM_IN_A_ROW:
                return True
        else:
            count = 0

    # checks horizontal
    count = 0
    for char in range(NUM_OF_COLUMNS):
        if grid[y][char] == color:
            count += 1
            if count == NUM_IN_A_ROW:
                return True
        else:
            count = 0

    # checks diagonal going down and right
    count = 0
    if y < x:
        xStartingPoint = 0
        yStartingPoint = abs(y - x)
        startingPoint = yStartingPoint
        endingPoint = NUM_OF_COLUMNS
    else:
        xStartingPoint = abs(y - x)
        yStartingPoint = 0
        startingPoint = xStartingPoint
        endingPoint = NUM_OF_ROWS

    for char in range(endingPoint - startingPoint):
        if grid[xStartingPoint + char][yStartingPoint + char] == color:
            count += 1
            if count == NUM_IN_A_ROW:
                return True
        else:
            count = 0

    # checks diagonal going down and left
    # count = 0
    # if y < x:
    #     xStartingPoint = y - 1
    #     yStartingPoint = NUM_OF_COLUMNS - 1
    #     startingPoint = xStartingPoint
    #     endingPoint = NUM_OF_ROWS
    # else:
    #     xStartingPoint = abs(y - x)
    #     yStartingPoint = 0
    #     startingPoint = yStartingPoint
    #     endingPoint = NUM_OF_COLUMNS

    # for char in range(NUM_OF_COLUMNS - y):
    #     if grid[xStartingPoint + char][yStartingPoint - char] == color:
    #         count += 1
    #         if count == NUM_IN_A_ROW:
    #             return True
    #     else:
    #         count = 0

    #checks for cat game
    for spot in range(NUM_OF_COLUMNS):
        if grid[0][spot] == EMPTY:
            return False
    return True

def main():
    NUM_OF_ROWS = 6
    NUM_OF_COLOMNS = 7
    MAX_MOVES = NUM_OF_ROWS * NUM_OF_COLOMNS
    playerOneName, playerTwoName = "", ""
    playerList = [[playerOneName, BLACK], [playerTwoName, RED]]
    totalMoves = 0
    playAgain = True

    welcome()
    for player in playerList:
        player[0] = getPlayerName()

    SCREEN.fill(FRAME_COLOR)
    grid = setGrid()

    while playAgain:
        moveCount(totalMoves, MAX_MOVES)
        playerPrompt(playerList)
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if pygame.key.name(e.key) == '0':
                    pygame.quit()
                    sys.quit()
                elif pygame.key.name(e.key) >= '1' and pygame.key.name(e.key) <= '7':
                    pressedKey = int(pygame.key.name(e.key))
                    for y in range(475, 49, -((CIRCLE_RADIUS*2) + BARRIER)):
                        tempCoordinates = (50 + ((pressedKey - 1)*85), y)
                        if tempCoordinates in grid:
                            totalMoves += 1
                            pygame.draw.circle(SCREEN, playerList[0][1], tempCoordinates, CIRCLE_RADIUS)
                            grid.remove(tempCoordinates)
                            switchPlayers(playerList)
                            break

            if totalMoves >= MAX_MOVES:
                playAgain = showMenu()
                SCREEN.fill(FRAME_COLOR)
                grid = setGrid()
                totalMoves = 0

main()