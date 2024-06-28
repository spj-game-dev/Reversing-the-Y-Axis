import pygame

class MathRect:
    def __init__(self, x, y, width, height, sdim):
        self.mrect = pygame.Rect(x, sdim[1]-y, width, height)
        
    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.mrect)
