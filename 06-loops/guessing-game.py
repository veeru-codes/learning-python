import random

random_number = random.randint(1, 10)
user_guess = int(input('Guess a number between 1 and 10: '))

while True:
    if user_guess < random_number:
        print('Too low, try again!')
        user_guess = int(input('Guess a number between 1 and 10: '))
    elif user_guess > random_number:
        print('Too high, try again!')
        user_guess = int(input('Guess a number between 1 and 10: '))
    else:
        print('You guessed it. You won!')
        play_again = input('Do you want to keep playing? (y/n) ')
        if play_again == 'y':
            random_number = random.randint(1, 10)
            user_guess = int(input('Guess a number between 1 and 10: '))
        else:
            print('Thanks for playing.')
            break
