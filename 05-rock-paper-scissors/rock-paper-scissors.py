# print('...rock...')
# print('...paper...')
# print('...scissors...')
# player1 = input("(Enter Player 1's choice): ")
# player2 = input("(Enter Player 2's choice): ")

# ----------------------------------------------------------------
# Version 1
# ----------------------------------------------------------------
# if player1 == 'rock' and player2 == 'paper':
#     print('SHOOT!')
#     print('Player 2 wins')
# elif player1 == 'rock' and player2 == 'scissors':
#     print('SHOOT!')
#     print('Player 1 wins')
# elif player1 == 'paper' and player2 == 'rock':
#     print('SHOOT!')
#     print('Player 1 wins')
# elif player1 == 'paper' and player2 == 'scissors':
#     print('SHOOT!')
#     print('Player 2 wins')
# elif player1 == 'scissors' and player2 == 'rock':
#     print('SHOOT!')
#     print('Player 2 wins')
# elif player1 == 'scissors' and player2 == 'paper':
#     print('SHOOT!')
#     print('Player 1 wins')
# elif player2 == player1:
#     print('SHOOT!')
#     print("It's a draw. Try again!")
# else:
#     print('Oh no. Something went wrong!')

# ----------------------------------------------------------------
# Version 2
# ----------------------------------------------------------------
# if player2 == player1:
#     print('SHOOT!')
#     print("It's a draw. Try again!")
# elif player1 == 'rock':
#     if player2 == 'paper':
#         print('Player 2 wins')
#     else:
#         print('Player 1 wins')
# elif player1 == 'paper':
#     if player2 == 'rock':
#         print('Player 1 wins')
#     else:
#         print('Player 2 wins')
# elif player1 == 'scissors':
#     if player2 == 'rock':
#         print('Player 2 wins')
#     else:
#         print('Player 1 wins')
# else:
#     print('Oh no. Something went wrong!')

# ----------------------------------------------------------------
# Version 3
# ----------------------------------------------------------------
from random import choice

print('...rock...')
print('...paper...')
print('...scissors...')
player1 = input("(Enter your choice): ").lower()
player2 = choice(['rock', 'paper', 'scissors'])
print('The computer plays: ', player2)
if player2 == player1:
    print('SHOOT!')
    print("It's a draw. Try again!")
elif player1 == 'rock':
    if player2 == 'paper':
        print('Computer wins')
    else:
        print('You win')
elif player1 == 'paper':
    if player2 == 'rock':
        print('You win')
    else:
        print('Computer wins')
elif player1 == 'scissors':
    if player2 == 'rock':
        print('Computer wins')
    else:
        print('You win')

else:
    print('Oh no. Something went wrong!')