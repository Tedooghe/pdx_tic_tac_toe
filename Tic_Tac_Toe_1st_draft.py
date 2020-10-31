class Game:
    def __init__(self,player1,player2):
        self.p1 = user
        self.p2 = 'Hal'
        self.board = [' ' for _ in range(9)]
        self.turn = 1

#assigns the user x and computer o

class Board:
    def __init__(self,board):
        self.board = board

    def __repr__(self):
#returns a pretty string representation of the game board
        ret = []
        for x in range(9):
            if x % 3 < 2:
                ret.append(self.board[x] + "|")
            else:
                ret.append(self.board[x] + '/n')
        return ''.join(ret) 
        
    
    def move(self, x, y, Player):
        if self.turn % 2 < 0:
            turn = self.player1


#place a token char string at a coodinate
#(top-left is 0,0)
#x is horiz / y is vert


    #def calc_winner():
#what token char string has won, or None


    #def is_full():
#returns true if game board is full


    #def is_game_over():
#returns true if board is full or a player has won


user = input('to play, enter your name here: ')
#player1 = Player(human, 'X')
#player2 = Player('Hal', 'O')
