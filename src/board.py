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
        def pawn_moves():
            """
            Calculate all possible moves for a pawn piece on a given square.

            Args:
                pecie (Piece): The pawn piece.
                row (int): The row index of the pawn piece.
                col (int): The column index of the pawn piece.
            """
            # Calculate the number of steps the pawn can take
            steps = 1 if pecie.moved else 2

            # Calculate the range of rows the pawn can move to
            start = row + pecie.dir
            end = row + (pecie.dir * (1 + steps))

            # Iterate over the possible rows the pawn can move to
            for possible_move_row in range(start, end, pecie.dir):
                # Check if the row is within the board range
                if Square.in_range(possible_move_row):
                    # Check if the square is empty
                    if self.squares[possible_move_row][col].is_empty():
                        # Create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new valid move
                        pecie.add_move(move)
                    else:
                        # If the square is not empty, stop the loop
                        break
                else:
                    # If the row is outside the board range, stop the loop
                    break

            # Calculate the possible diagonal moves
            possible_move_row = row + pecie.dir
            possible_move_cols = [col + 1, col - 1]

            # Iterate over the possible diagonal moves
            for possible_move_col in possible_move_cols:
                # Check if the square is within the board range
                if Square.in_range(possible_move_row, possible_move_col):
                    # Check if the square is occupied by a rival piece
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(pecie.color):
                        # Create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new valid move
                        pecie.add_move(move)

        def knight_moves():
            """
            Calculate all possible moves for a knight piece on a given square.

            Args:
                pecie (Piece): The knight piece.
                row (int): The row index of the knight piece.
                col (int): The column index of the knight piece.
            """
            # 8 possible moves for a knight
            possible_moves = [
                (row - 2, col + 1),  # Move up and two squares right
                (row - 2, col - 1),  # Move up and two squares left
                (row - 1, col + 2),  # Move up and one square right
                (row - 1, col - 2),  # Move up and one square left
                (row + 2, col + 1),  # Move down and two squares right
                (row + 2, col - 1),  # Move down and two squares left
                (row + 1, col + 2),  # Move down and one square right
                (row + 1, col - 2),  # Move down and one square left
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    # Check if the square is empty or occupied by a rival piece
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(pecie.color):
                        # Create initial and final move squares
                        initial = Square(row, col)
                        # TODO: piece=pecie
                        final = Square(possible_move_row, possible_move_col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new valid move
                        pecie.add_move(move)
                        pecie.add_move(move)

        def straight_line_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    # Check if the square is within the board range
                    if Square.in_range(possible_move_row, possible_move_col):
                        # create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a possible new move
                        move = Move(initial, final)

                        if self.squares[possible_move_row][possible_move_col].is_empty():
                            # append new valid move
                            pecie.add_move(move)
                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(pecie.color):
                            # append new valid move
                            pecie.add_move(move)
                            break
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(pecie.color):
                            break

                    else:
                        break
                    # incremaneting the incrs
                    possible_move_row += row_incr
                    possible_move_col += col_incr

                    # Calculate all possible moves for a pawn piece on a given square.
                    # This function is called when the piece is a Pawn.

        def king_moves():
            adjs = [
                (row - 1, col + 0),
                (row - 1, col + 1),
                (row - 0, col + 1),
                (row + 1, col + 1),
                (row + 1, col + 0),
                (row + 1, col - 1),
                (row - 0, col - 1),
                (row - 1, col - 1),
            ]

            # normal moves
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(pecie.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        pecie.add_move(move)
                        
            # TODO: castling moves
            # castling moves
            # king castling
            # queen castling

        if isinstance(pecie, Pawn):
            """
            Calculate all possible moves for a pawn piece on a given square.

            Args:
                pecie (Piece): The pawn piece.
                row (int): The row index of the pawn piece.
                col (int): The column index of the pawn piece.
            """
            pawn_moves()

        elif isinstance(pecie, Knight):
            """
            Calculate all possible moves for a knight piece on a given square.

            Args:
                pecie (Piece): The knight piece.
                row (int): The row index of the knight piece.
                col (int): The column index of the knight piece.
            """
            knight_moves()

        elif isinstance(pecie, Bishop):
            """
            Calculate all possible moves for a bishop piece on a given square.

            The bishop moves in straight lines in any direction horizontally
            or vertically. This function calculates the straight line moves
            in the four possible directions.

            Args:
                pecie (Piece): The bishop piece.
                row (int): The row index of the bishop piece.
                col (int): The column index of the bishop piece.
            """
            # Calculate the straight line moves in the four possible directions
            straight_line_moves([
                # Move diagonally up and to the right
                (1, 1),
                # Move diagonally up and to the left
                (-1, 1),
                # Move diagonally down and to the right
                (1, -1),
                # Move diagonally down and to the left
                (-1, -1),
            ])

        elif isinstance(pecie, Rook):
            """
            Calculate all possible moves for a rook piece on a given square.

            The rook moves in straight lines in any direction horizontally
            or vertically. This function calculates the straight line moves
            in the four possible directions.

            Args:
                pecie (Piece): The rook piece.
                row (int): The row index of the rook piece.
                col (int): The column index of the rook piece.
            """
            # Calculate the straight line moves in the four possible directions
            straight_line_moves([
                # Move horizontally to the left
                (-1, 0),
                # Move horizontally to the right
                (1, 0),
                # Move vertically upwards
                (0, -1),
                # Move vertically downwards
                (0, 1),
            ])

        elif isinstance(pecie, Queen):
            """
            Calculate all possible moves for a queen piece on a given square.

            The queen moves in straight lines in any direction horizontally,
            vertically, or diagonally. This function calculates the straight
            line moves in the eight possible directions.

            Args:
                pecie (Piece): The queen piece.
                row (int): The row index of the queen piece.
                col (int): The column index of the queen piece.
            """
            # Calculate the straight line moves in the eight possible directions
            straight_line_moves([
                # Move diagonally up and to the right
                (1, 1),
                # Move diagonally up and to the left
                (-1, 1),
                # Move diagonally down and to the right
                (1, -1),
                # Move diagonally down and to the left
                (-1, -1),
                # Move horizontally to the left
                (-1, 0),
                # Move horizontally to the right
                (1, 0),
                # Move vertically upwards
                (0, -1),
                # Move vertically downwards
                (0, 1),
            ])

        elif isinstance(pecie, King):
            king_moves()

    def _add_pieces(self, color):
        """
        Add pieces to the board based on the given color.

        Args:
            color (str): The color of the pieces to be added.
        """
        # Determine the row indexes for the pawns and the other pieces
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # Add pawns to the board
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Add knights to the board
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Add bishops to the board
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # Add rooks to the board
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Add queen to the board
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # Add king to the board
        self.squares[row_other][4] = Square(row_other, 4, King(color))
        self.squares[2][4] = Square(2, 4, King(color))
