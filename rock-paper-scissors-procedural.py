# Scissors beats Paper
# Paper beats Rock
# Rock Beats Scissors
import random

while True:
    # ask the user for input and assign it to a variable
    # add in some error checking
    player1 = ''
    while player1 not in ['rock','paper','scissors']:
        player1 = input('What hand shape do you choose? (rock,paper,scissors)')
    # create the computer player input
    hand_shapes = ['rock','paper','scissors']
    player2 = hand_shapes[random.randint(0,2)]


    # check that input against the winning combinations
    winning_combinations = {
        'rock':'paper',
        'paper':'scissors',
        'scissors':'paper'
    }
    result = ''
    # loop over winning_combinations and check to see who won
    for key in winning_combinations:
        if player1 == key and player2 == winning_combinations[key]:
            result = 'You Won'
            break
        elif player2 == key and player1 == winning_combinations[key]:
            result = 'You Lost'
            break
        else:
            result = 'Draw'
            break

    print(result)
    # print out the result (Win,Lose,Draw)
    play_again = ''
    while play_again not in ['y','n']:
        play_again = input('Would you like to play again?')

    if play_again.lower() == 'n':
        break
