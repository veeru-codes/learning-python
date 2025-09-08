# guessing game
from random import randint
num = randint(1, 10)
player_guess = None

while True:
    player_guess = int(input('guess a number between 1 and 10: '))
    if player_guess < num:
        print('1you guessed too low! try again!')
    elif player_guess > num:
        print('you guessed too high! try again!')
    else:
        print('you guessed it! you win!')
        play_again = input('do you want to play again? (y/n): ')
        if play_again == 'y':
            num = randint(1, 10)
            player_guess = None
        else:
            input('thanks for playing!')
            break


