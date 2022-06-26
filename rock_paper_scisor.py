
from getpass import getpass
import os
from random import randint
from time import sleep

game = 'yes'
os.system('cls')
print('\n\n\n\n')
l1 = [0]
l2 = [0]
count = 0
print("--------------------WELCOME TO ROCK PAPER SCISSOR GAME--------------------".rjust(100))
print('\n\n\n')
while game == 'yes' or game =='y':
    p1 = getpass('Player 1 choice:- '.rjust(100)).lower().strip()
    #get take string as a password which do not show to the user
    print('\n\n')
    p2 = getpass('Player 2 choice:- '.rjust(100)).lower().strip()

    p1_won = [
        (p1 == 'rock' and p2==  'scissor'),
        (p1 == 'paper' and p2=='rock'),
        (p1 == 'scissor' and p2== 'paper')
    ]
    print('\n\n\t\t Processing',end='')
    for i in range (randint(5,9)):
        print('.',end = '',flush = True)
        sleep(1)

    print(f"Choice of player 1 :- {p1}".center(50))    
    print('\n\n\n ')
    print(f"Choice of Player 2 :-{p2}".center(50))
    print('\n\n\n')

    if any(p1_won):
        print("Player 1 won the game ".upper().rjust(100))
        count+=1
        l1.append(count)
    elif p1 == p2:
        print("game is tie".upper().rjust(100))
    else:
        print("player 2 won the game".upper().rjust(100))
        count+=1
        l2.append(count)
    print('\n\n\n')
    game = input('--------------------Do you want to continue? ~----------------------'.rjust(100))
    game = game.lower()

    os.system('cls')
    
print("--------------------------Total winning of players is--------------------------".rjust(100))
print("Player 1 :- ",l1[-1])
print("Player 2 :- ",l2[-1])
if l1>l2:
    print("----------------Player 1 Won more times then player 2!!-------------------------".rjust(100))
elif l2>l1:
    print("----------------Player 2 Won more times then player 1!!-------------------------".rjust(100))
else:
    print("TIE")