

class Square:

    def __init__(self, row, col, peice=None):
        self.row = row
        self.col = col
        self.peice = peice

    def has_peice(self):
        return self.peice != None

    def is_empty(self):
        return not self.has_peice()

    def has_team_piece(self, color):
        return self.has_peice() and self.peice.color == color

    def has_rival_piece(self, color):
        return self.has_peice() and self.peice.color != color

    def isempty_or_rival(self, color):
        return self.is_empty() or self.has_rival_piece(color)

    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
