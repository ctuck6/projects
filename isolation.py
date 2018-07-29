import sys
import random
import time
from colorama import *
init(autoreset = True)
from termcolor import colored

game_status = "Game in progress! Good luck, may the odds be with you both!"
p1color = "red"
p2color = "yellow"

def clear():
    sys.stderr.write("\x1b[2J\x1b[H")

def welcome():
    global player1, player2, row1, row2, row3, row4, column
    row1 = ['X', '-', '-', '-']
    row2 = ['-', '-', '-', '-']
    row3 = ['-', '-', '-', '-']
    row4 = ['-', '-', '-', 'O']
    column = [row1, row2, row3, row4]

    print("Welcome To Isolation!")
    # version = int(input("Do you want to play ANOTHER PLAYER(1) or THE COMPUTER(2)? Enter '1' or '2': "))
    # while version != 1 or version != 2:
    #     if version == 1:
    player1 = input("Player 1 enter a name: ")
    player2 = input("Player 2 enter a name: ")
    print('\n')
    multiplayer()
        # elif version == 2:
        #     player1 = input("Player 1 enter a name: ")
        #     player2 = "The Computer"
        #     auto()
        # else:
        #     version = int(input("Really... REALLY? You KNOW that's not a choice! Enter '1' or '2': "))

def display():
    print(Fore.WHITE + "--------------------")
    print(Fore.WHITE + "   | 1 | 2 | 3 | 4 |")
    print(Fore.WHITE + "--------------------")
    for i in range(0, 4):
        print('', chr(65 + i), '|', column[i][0], '|', column[i][1], '|', column[i][2], '|', column[i][3], '|')
        print(Fore.WHITE + "--------------------")
    print('\n')

def moveValidation():
    #checks verticals
    for y in range(0, 4):
        a = [column[[][]]
        if a.count(colored("O", p1color, attrs=['blink', 'bold'])) == 1 and a.count(colored("O", p1color, attrs=['dark'])) == 3:
            column[0][y] = column[1][y] = column[2][y] = column[3][y] = colored("O", p1color, "on_cyan", attrs=['blink', 'bold'])
            oneWin()
        elif a.count(colored("O", p2color, attrs=['blink', 'bold'])) == 1 and a.count(colored("O", p2color, attrs=['dark'])) == 3:
            column[x][y] = column[x + 1][y] = column[x + 2][y] = column[x + 3][y] = colored("O", p2color, "on_cyan", attrs=['blink', 'bold'])
            twoWin()
    #checks horizontals
    for y in range(0, 4):
        b = [column[x][y], column[x][y + 1], column[x][y + 2], column[x][y + 3]]
        if b.count(colored("O", p1color, attrs=['blink', 'bold'])) == 1 and b.count(colored("O", p1color, attrs=['dark'])) == 3:
            column[x][y] = column[x][y + 1] = column[x][y + 2] = column[x][y + 3] = colored("O", p1color, "on_cyan", attrs=['blink', 'bold'])
            oneWin()
        elif b.count(colored("O", p2color, attrs=['blink', 'bold'])) == 1 and b.count(colored("O", p2color, attrs=['dark'])) == 3:
            column[x][y] = column[x][y + 1] = column[x][y + 2] = column[x][y + 3] = colored("O", p2color, "on_cyan", attrs=['blink', 'bold'])
            twoWin()
    #checks right diagonals
    for y in range(0, 4):
        c = [column[x][y], column[x + 1][y + 1], column[x + 2][y + 2], column[x + 3][y + 3]]
        if c.count(colored("O", p1color, attrs=['blink', 'bold'])) == 1 and c.count(colored("O", p1color, attrs=['dark'])) == 3:
            column[x][y] = column[x + 1][y + 1] = column[x + 2][y + 2] = column[x + 3][y + 3] = colored("O", p1color, "on_cyan", attrs=['blink', 'bold'])
            oneWin()
        elif c.count(colored("O", p2color, attrs=['blink', 'bold'])) == 1 and c.count(colored("O", p2color, attrs=['dark'])) == 3:
            column[x][y] = column[x + 1][y + 1] = column[x + 2][y + 2] = column[x + 3][y + 3] = colored("O", p2color, "on_cyan", attrs=['blink', 'bold'])
            twoWin()
    #checks left diagonals
    for y in range(0, 4):
        d = [column[x][y], column[x + 1][y - 1], column[x + 2][y - 2], column[x + 3][y - 3]]
        if d.count(colored("O", p1color, attrs=['blink', 'bold'])) == 1 and d.count(colored("O", p1color, attrs=['dark'])) == 3:
            column[x][y] = column[x + 1][y - 1] = column[x + 2][y - 2] = column[x + 3][y - 3] = colored("O", p1color, "on_cyan", attrs=['blink', 'bold'])
            oneWin()
        elif d.count(colored("O", p2color, attrs=['blink', 'bold'])) == 1 and d.count(colored("O", p2color, attrs=['dark'])) == 3:
            column[x][y] = column[x + 1][y - 1] = column[x + 2][y - 2] = column[x + 3][y - 3] = colored("O", p2color, "on_cyan", attrs=['blink', 'bold'])
            twoWin()
    #checks for cat game
    for i in range(0, 4)
        e = [column[i][0], column[i][1], column[i][2], column[i][3]]
        if i == 3 and e.count('-') == 0:
            gameStatus = "Tie game! No one wins but hey, no one loses either!"
            display()
            print(gameStatus)
            newGame = input("Press 'y' to play again, or any other key to quit: ")
            newGame.lower()
            if newGame == 'y':
                welcome()
            else:
                quit()
        elif e.count('-') > 0:
            break

def multiplayer():
    print(game_status, '\n')
    display()
    column[0][0], column[3][3] = 'B', 'B';
    user2 = "D4" # bypasses variable error
    while True:
        user1 = str(input("{} make your move(Ex. B2). If you want to quit, enter 0: ".format(player1)))
        if user1 == '0':
            quit()
        while (ord(user1[0]) not in range(65, 69)) and (user1[1] not in range(1, 5)):
            user1 = str(input("Not valid! {} make your move(Ex. B2). If you want to quit, enter 0: ".format(player1)))
        while str(column[ord(str(user1[0])) - 65][int(user1[1]) - 1]) != '-':
            user1 = str(input("Spot taken! Try again, or enter 0 to quit: ".format(player1)))
            if user1 == '0':
                quit()
        column[ord(str(user1[0])) - 65][int(user1[1]) - 1] = 'X'
        clear()
        # check()
        display()
        column[ord(str(user2[0])) - 65][int(user2[1]) - 1] = 'B'

        user2 = str(input("{} make your move(Ex. B2). If you want to quit, enter 0: ".format(player2)))
        if user2 == '0':
            quit()
        while (ord(user2[0]) not in range(65, 69)) and (user2[1] not in range(1, 5)):
            user2 = str(input("Not valid! {} make your move(Ex. B2). If you want to quit, enter 0: ".format(player2)))
        while str(column[ord(str(user2[0])) - 65][int(user2[1]) - 1]) != '-':
            user2 = str(input("Spot taken! Try again, or enter 0 to quit: ".format(player2)))
            if user2 == '0':
                quit()
        column[ord(str(user2[0])) - 65][int(user2[1]) - 1] = 'O'
        clear()
        # check()
        display()
        column[ord(str(user1[0])) - 65][int(user1[1]) - 1] = 'B'
        
if __name__ == '__main__':
    welcome()