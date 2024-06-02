import pygame

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Board dimensions
ROWS = 8
COLS = 8
SQSIZE = WIDTH // COLS


class Dragger:

    def __init__(self):
        self.peice = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initialRow = 0
        self.initialCol = 0

    def update_blit(self, surface):
        self.peice.set_texture(size=128)
        texture = self.peice.texture

        img = pygame.image.load(texture)

        img_center = (self.mouseX, self.mouseY)
        self.peice.texture_rect = img.get_rect(center=img_center)

        surface.blit(img, self.peice.texture_rect)

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initialRow = pos[1] // SQSIZE
        self.initialCol = pos[0] // SQSIZE

    def drag_peice(self, piece):
        self.peice = piece
        self.dragging = True

    def undrag_piece(self):
        self.peice = None
        self.dragging = False
