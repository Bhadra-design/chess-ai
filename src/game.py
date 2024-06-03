import pygame

from board import Board
from dragger import Dragger

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Board dimensions
ROWS = 8
COLS = 8
SQSIZE = WIDTH // COLS


class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

# Show Methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # peice ?
                if self.board.squares[row][col].has_peice():
                    peice = self.board.squares[row][col].peice

                    # all peices except dragging peice
                    if peice != self.dragger.peice:
                        peice.set_texture(size=80)
                        img = pygame.image.load(peice.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        peice.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, peice.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.peice

            # loop thru all valid moves
            for move in piece.moves:
                # color
                color = '#C86464' if move.final.row + move.final.col % 2 == 0 else '#C84646'
                # cricle
                cricle = move.final.col * SQSIZE + \
                    SQSIZE // 2, move.final.row * SQSIZE + SQSIZE // 2
                # blit
                pygame.draw.circle(surface, color, cricle, 20)
