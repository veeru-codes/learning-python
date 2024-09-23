from random import choice

player_wins = 0
computer_wins = 0
winning_score = 5

while player_wins < winning_score and computer_wins < winning_score:
    print('...rock...')
    print('...paper...')
    print('...scissors...')

    player = input("(Enter your choice): ").lower()
    computer = choice(['rock', 'paper', 'scissors'])
    print('The computer plays: ', computer)

    if computer == player:
        print('SHOOT!')
        print("It's a draw. Try again!")
    elif player == 'rock':
        if computer == 'paper':
            print('Computer wins')
            computer_wins += 1
        else:
            print('You win')
            player_wins += 1
    elif player == 'paper':
        if computer == 'rock':
            print('You win')
            player_wins += 1
        else:
            print('Computer wins')
            computer_wins += 1
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer wins')
            computer_wins += 1
        else:
            print('You win')
            player_wins += 1

    else:
        print('Oh no. Something went wrong!')

print(
    f"Final Scores... Player score: {
        player_wins} - Computer score: {computer_wins}"
)
