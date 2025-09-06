from random import choice

print('...rock...paper...scissors...')
player_one_choice = input("enter player 1's choice: ").lower()
computer_choice = choice(['rock', 'paper', 'scissors']).lower()
print(f'the computer plays: {computer_choice}')

if player_one_choice and computer_choice:
    if player_one_choice == 'rock' and computer_choice == 'scissors':
        print('player 1 wins!')
    elif player_one_choice == 'scissors' and computer_choice == 'paper':
        print('player 1 wins!')
    elif player_one_choice == 'paper' and computer_choice == 'rock':
        print("player 1 wins!")
    elif player_one_choice == computer_choice:
        print("it's a tie!")
    else:
        print('player 2 wins!')
else:
    print('something went wrong')