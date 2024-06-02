

class Square:

    def __init__(self, row, col, peice=None):
        self.row = row
        self.col = col
        self.peice = peice

    def has_peice(self):
        return self.peice != None