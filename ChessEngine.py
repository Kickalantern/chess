#Stores all info on current state of a chess game. determines valid movements at current state. Also keeps a move log.

class GameState():
    def __init__(self):
        #board is 8x8 2-dimensional list. Each element of list has two characters. 
        #first character represents piece colour. Second represents type of piece
        #"--" represents empty space
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"]
            ["bP","bP","bP","bP","bP","bP","bP","bP"]
            ["--","--","--","--","--","--","--","--"]
            ["--","--","--","--","--","--","--","--"]
            ["--","--","--","--","--","--","--","--"]
            ["--","--","--","--","--","--","--","--"]
            ["wP","wP","wP","wP","wP","wP","wP","wP"]
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]