print('...rock, paper, scissors...')
player_one_choice = input("enter player 1's choice: ")
player_two_choice = input("enter player 2's choice: ")

if player_one_choice and player_two_choice:
    if player_one_choice == 'rock' and player_two_choice == 'scissors':
        print('player 1 wins!')
    elif player_one_choice == 'scissors' and player_two_choice == 'paper':
        print('player 1 wins!')
    elif player_one_choice == 'paper' and player_two_choice == 'rock':
        print("player 1 wins!")
    elif player_one_choice == player_two_choice:
        print("it's a tie!")
    else:
        print('player 2 wins!')
else:
    print('something went wrong')


