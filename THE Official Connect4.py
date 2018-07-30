from termcolor import colored, cprint
import sys

global PLAYER_ONE_COLOR, PLAYER_TWO_COLOR, MAIN_COLOR
global EMPTY
global NUM_OF_ROWS, NUM_OF_COLUMNS, NUM_IN_A_ROW, NUM_OF_PLAYERS
PLAYER_ONE_COLOR, PLAYER_TWO_COLOR, MAIN_COLOR = "red", "yellow", "white"
EMPTY = ' '
NUM_OF_ROWS, NUM_OF_COLUMNS, NUM_IN_A_ROW, NUM_OF_PLAYERS = 6, 7, 4, 2

def clear():
    sys.stderr.write("\x1b[2J\x1b[H")

def chooseMode():
    # version = int(input("Do you want to play ANOTHER PLAYER(1) or THE COMPUTER(2)? Enter '1' or '2': "))
    # while version != 1 or version != 2:
        # if version == 1:
            # return 1
        # elif version == 2:
            # return 2
        # else:
        #     version = int(input("Really... REALLY? You KNOW that's not a choice! Enter '1' or '2': "))
    return 1

def createGrid():
    return [[EMPTY for column in range(NUM_OF_COLUMNS)] for row in range(NUM_OF_ROWS)]

def displayGrid(grid, color):
    if color == MAIN_COLOR:
        for num in range(NUM_OF_COLUMNS):
            print(' ', end = "", flush = True)
            print(colored("  " + str(num + 1) + "  ", color), end = "", flush = True)
        print(' ')
    boarder = ""
    for num in range(NUM_OF_COLUMNS):
        boarder += colored('-', color)
        boarder += colored("-----", color)
    boarder += colored('-', color)
    print(boarder)
    for x in range(NUM_OF_ROWS):
        for y in range(NUM_OF_COLUMNS):
            print(colored("¦  {}  ".format(grid[x][y]), color), end = "", flush = True)
            if y == NUM_OF_COLUMNS - 1:
                print(colored("¦\n" + boarder, color))
    print('\n')

def win(player, color):
    if player is not "No one":
        print(colored("Connect 4! Game Over!", color, attrs = ["bold"]))
        print(colored("{} wins!".format(player), color, attrs = ["bold"]))
    else:
        print(colored("Tie game! No one wins but hey, no one loses either!", color, attrs = ["bold"]))
    newGame = input("Enter 'y' to play again, any other key to quit: ").lower()
    if newGame == 'y':
        main()
    else:
        quit()

def checkForWinner(grid, x, y, player, color):
    # checks vertical
    count, startingPoint = 0, 0
    for char in range(NUM_OF_ROWS):
        if grid[char][x] == colored('O', color, attrs = ["dark"]):
            count += 1
            if count == NUM_IN_A_ROW:
                for newChar in range(startingPoint, char + 1):
                    grid[newChar][x] = colored('O', color, "on_cyan", attrs = ["blink", "bold"])
                return True
        else:
            startingPoint = char + 1
            count = 0

    # checks horizontal
    count, startingPoint = 0, 0
    for char in range(NUM_OF_COLUMNS):
        if grid[y][char] == colored('O', color, attrs = ["dark"]):
            count += 1
            if count == NUM_IN_A_ROW:
                for newChar in range(startingPoint, char + 1):
                    grid[y][newChar] = colored('O', color, "on_cyan", attrs = ["blink", "bold"])
                return True
        else:
            startingPoint = char + 1
            count = 0

    # checks diagonal going down and right
    count, smaller, highlightingStart = 0, min(x, y), 0
    if smaller == y:
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
        if grid[xStartingPoint + char][yStartingPoint + char] == colored('O', color, attrs = ["dark"]):
            count += 1
            if count == NUM_IN_A_ROW:
                for newChar in range(highlightingStart, char + 1):
                    grid[xStartingPoint + newChar][yStartingPoint + newChar] = colored('O', color, "on_cyan", attrs = ["blink", "bold"])
                return True
        else:
            highlightingStart = char + 1
            count = 0

    # # checks diagonal going down and left
    # temp = ""
    # for spot in range(NUM_OF_COLUMNS):
    #     temp += grid[y][spot]
    # if temp.count(colored('O', color, attrs = ["dark"])) == NUM_IN_A_ROW:
    #     for char in range(NUM_OF_COLUMNS):
    #         if grid[y][char] == colored('O', color, attrs = ["dark"]):
    #             grid[y][char] = colored('O', color, "on_cyan", attrs = ["blink", "bold"])
    #     return True

    #checks for cat game
    for spot in range(NUM_OF_COLUMNS):
        if grid[0][spot] == EMPTY:
            return False
    return True
        
def playerMove(grid, playerList):
    userMove = int(input("{}, place your chip in a column. Enter '0' to quit the game: ".format(playerList[0][0])))
    print('\n')
    while userMove not in range(1, NUM_OF_COLUMNS + 1) or grid[0][userMove - 1] != EMPTY:
        if userMove == 0:
            quit()
        elif grid[0][userMove - 1] != EMPTY:
            userMove = int(input("{}, that column is full. Try again, or enter '0' to quit the game: ".format(playerList[0][0])))
        else:
            print("That column is non-existent! Try again!")
            userMove = int(input("{}, place your chip in a column. Enter '0' to quit the game: ".format(playerList[0][0])))
            print('\n')    
        
    for spot in range(NUM_OF_ROWS - 1, -1, -1):
        if grid[spot][userMove - 1] == EMPTY:
            grid[spot][userMove - 1] = colored('O', playerList[0][1], attrs = ["blink", "bold"])
            break

    return [userMove - 1, spot]

def switchPlayers(playerList):
    playerList[0], playerList[1] = playerList[1], playerList[0]

def main():
    playerOne, playerTwo = "", ""
    playerList = [[playerOne, PLAYER_ONE_COLOR], [playerTwo, PLAYER_TWO_COLOR]]
    gridColor = MAIN_COLOR
    winningPlayer = "No one"
    maxMoves, numOfMoves = (NUM_OF_ROWS * NUM_OF_COLUMNS), 0
    winner = False

    print("Welcome to connect 4!")
    choice = chooseMode()
    if choice == 1:
        for i in range(NUM_OF_PLAYERS):
            playerList[i][0] = input("Player {} enter a name: ".format(i + 1))
        grid = createGrid()
        print("\nGame in progress! Good luck, may the odds be with you both!\n")
        displayGrid(grid, MAIN_COLOR)
        while not winner:
            coordinates = playerMove(grid, playerList)
            # clear()
            displayGrid(grid, MAIN_COLOR)
            grid[coordinates[1]][coordinates[0]] = colored('O', playerList[0][1], attrs = ["dark"])
            numOfMoves += 1
            winner = checkForWinner(grid, coordinates[0], coordinates[1], playerList[0][0], playerList[0][1])
            if not winner:
                switchPlayers(playerList)
        if numOfMoves < maxMoves:
            winningPlayer = playerList[0][0]
            gridColor = playerList[0][1]
        displayGrid(grid, gridColor)
        win(winningPlayer, gridColor)
    else:
        # auto()
        pass



if __name__ == "__main__":
    main()

