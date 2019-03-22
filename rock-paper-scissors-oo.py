import random

class Shape:
    def __init__(self,shape=''):
        if shape == '':
            self.shape = ['rock','paper','scissors'][random.randint(1,2)]
        else:
            self.shape = shape

class Game:

    def print_result(self,winner,player1,player2):
        print ("You: " + player1.shape)
        print ("Computer: " + player2.shape)
        print(winner)

    def check_winner(self,player1,player2):
        winning_combinations = {
            'rock':'scissors',
            'paper':'rock',
            'scissors':'paper'
        }
        for key in winning_combinations:
            if player1.shape == key and player2.shape == winning_combinations[key]:
                return "You Won"
            if player2.shape == key and player1.shape == winning_combinations[key]:
                return "You Lost"
            if (player1.shape == player2.shape):
                return "Draw"
        return winner


    def play_again(self):
        play_again = ''
        while play_again not in ['y','n']:
            play_again = input('Would you like to play again?')

        if play_again.lower() == 'y':
            self.play()
        else:
            print('Good Bye')

    def play(self):
        player1 = Shape(shape=input('What shape do you choose?(rock,paper,scissors)'))
        player2 = Shape()
        winner = self.check_winner(player1,player2)
        self.print_result(winner,player1,player2)
        self.play_again()



game = Game()
game.play()
