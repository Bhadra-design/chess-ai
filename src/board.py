from square import Square
from piece import *
from move import Move

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Board dimensions
ROWS = 8
COLS = 8
SQSIZE = WIDTH // COLS


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def calc_moves(self, pecie, row, col):
        '''
        Calculate all possible moves (leagal moves) for a given piece on a given square
        '''

        def knight_moves():
            # 8 possible moves for a knight
            possible_moves = [
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row - 1, col + 2),
                (row - 1, col - 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col + 2),
                (row + 1, col - 2),
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(pecie.color):
                        # create a sqaure for new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # TODO: piece=pecie
                        # create a new move
                        move = Move(initial, final)
                        # append new valid move
                        pecie.add_move(move)
                
        if isinstance(pecie, Pawn):
            pass

        elif isinstance(pecie, Knight):
            knight_moves()

        elif isinstance(pecie, Bishop):
            pass

        elif isinstance(pecie, Rook):
            pass

        elif isinstance(pecie, Queen):
            pass

        elif isinstance(pecie, King):
            pass

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
