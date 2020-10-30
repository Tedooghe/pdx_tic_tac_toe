class Player:
    def __init__(self,name,token):
        self.name = name
        self.token = token # X or O
    

#assigns the user x and computer o

class Board:
    def __init__(self,board):
        self.board = board


    def __repr__():
#returns a pretty string representation of the game board
    print(board)


    def move(x, y, Player):
#place a token char string at a coodinate
#(top-left is 0,0)
#x is horiz / y is vert


    def calc_winner():
#what token char string has won, or None


    def is_full():
#returns true if game board is full


    def is_game_over():
#returns true if board is full or a player has won

human = input('to play, enter your name here: ')
player1 = Player(human, 'X')
player2 = Player('Hal', 'O')
