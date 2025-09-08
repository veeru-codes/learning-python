from random import choice
print('...rock...paper...scissors...')
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f'player score: {player_wins} - computer score: {computer_wins}')
    player_choice = input('player choice: ').lower()
    computer_choice = choice(('rock', 'scissors', 'paper'))
    print(f'computer choice: {computer_choice}')
    if player_choice == computer_choice:
        continue
    elif player_choice == 'rock' and computer_choice == 'scissors':
        player_wins += 1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        player_wins += 1
    elif player_choice == 'paper' and computer_choice == 'rock':
        player_wins += 1
    else:
        computer_wins += 1

print(f'final scores: player score: {player_wins} - computer score: {computer_wins}')
if player_wins == 3:
    print('player wins!')
elif computer_wins == 3:
    print('computer wins!')
else:
    print('it is a tie')