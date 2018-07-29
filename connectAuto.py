# def auto():
#     global start
#     start = time.time()
#     print(gameStatus, "\n")
#     display()
#     while True:
#         user1 = int(input("{}, place your chip in a column. Enter 0 to quit the game: ".format(player1)))
#         print('\n')
#         while user1 not in range(1, 8):
#             if user1 == 0:
#                 quit()
#             else:
#                 print("That column is non-existent! Try again!")
#                 user1 = int(input("{}, place your chip in a column. Enter 0 to quit the game: ".format(player1)))
#                 print('\n')
#         empty = False
#         while empty == False:
#             for i in range(0, 6):
#                 if column[5][user1 - 1] != " ":
#                     user1 = int(input("{}, that column is full. Try again, or enter 0 to quit the game: ".format(player1)))
#                     break
#                 elif column[i][user1 - 1] == " ":
#                     column[i][user1 - 1] = (Fore.RED + Style.BRIGHT + "O")
#                     empty = True
#                     break
#         check()
#         display()
#         column[i][user1 - 1] = (Fore.RED + "O")
#         #determines whether the game will let the person win or block them! Can't make the game TOO difficult
#         difficulty = random.randrange(1, 6)
#         if difficulty in range(1, 5):
#             user2 = random.randrange(0, 7)
#             yes = False
#             for x in range(0, 3):
#                 if yes:
#                     break
#                 for y in range(0, 7):
#                     s = [column[x][y], column[x + 1][y], column[x + 2][y], column[x + 3][y]]
#                     #blocks vertical
#                     if (s.count((Fore.YELLOW + "O")) == 3 or s.count((Fore.RED + "O")) == 3) and (s.count(" ") == 1):
#                         user2 = y
#                         yes = True
#                         break
#             for x in range(0, 6):
#                 if yes:
#                     break
#                 for y in range(0, 4):
#                     r = [column[x][y], column[x][y + 1], column[x][y + 2], column[x][y + 3]]
#                     #blocks horizontal
#                     if (r.count((Fore.YELLOW + "O")) == 3 or r.count((Fore.RED + "O")) == 3) and (r.count(" ") == 1):
#                         for i in range(0, 4):
#                             if x > 0:
#                                 if r[i] == " " and (column[x - 1][y + i] != " "):
#                                     user2 = y + i
#                                     yes = True
#                                     break
#                             elif r[i] == " ":
#                                 user2 = y + i
#                                 yes = True
#                                 break
#             for x in range(0, 3):
#                 if yes:
#                     break
#                 for y in range(0, 4):
#                     t = [column[x][y], column[x + 1][y + 1], column[x + 2][y + 2], column[x + 3][y + 3]]
#                     #blocks diagonal going right
#                     if (t.count((Fore.YELLOW + "O")) == 3 or t.count((Fore.RED + "O")) == 3) and (t.count(" ") == 1):
#                         for i in range(0, 4):
#                             if (x > 0):
#                                 if t[i] == " " and (column[x - 1][y + i] != " "):
#                                     user2 = y + i
#                                     yes = True
#                                     break
#                             elif t[i] == " ":
#                                 user2 = y + i
#                                 yes = True
#                                 break
#             for x in range(0, 3):
#                 if yes:
#                     break
#                 for y in range(6, 2, -1):
#                     v = [column[x][y], column[x + 1][y - 1], column[x + 2][y - 2], column[x + 3][y - 3]]
#                     #blocks diagonal going left
#                     if (v.count((Fore.YELLOW + "O")) == 3 or v.count((Fore.RED + "O")) == 3) and (v.count(" ") == 1):
#                         for i in range(3, -1, -1):
#                             if (x > 0):
#                                 if v[i] == " " and (column[x - 1][y - i] != " "):
#                                     user2 = y - i
#                                     yes = True
#                                     break
#                             elif v[i] == " ":
#                                 user2 = y - i
#                                 yes = True
#                                 break
#             column[i][user2] = (Fore.YELLOW + Style.BRIGHT + "O")
#         else:
#             user2 = random.randrange(0, 7)
#             empty = False        
#             while empty == False:
#                 for i in range(0, 6):
#                     if column[5][user2] != " ":
#                         user2 = random.randrange(0, 7)
#                         break
#                     elif column[i][user2] == " ":
#                         column[i][user2] = (Fore.YELLOW + Style.BRIGHT + "O")
#                         empty = True
#                         break
#         check()
#         display()
#         column[i][user2] = (Fore.YELLOW + "O")