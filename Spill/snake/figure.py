import pygame

class Figure():
    def __init__(self, x:int, y:int, color, width:int = 48) -> None:
        self.width = width
        self.surface = pygame.Surface((self.width, self.width))
        self.rect = self.surface.get_rect()
        self.surface.fill(color)
        self.x = x
        self.y = y
        self.color = color

    def give_coordinates(self):
        self.rect.centerx = self.x * 50 + 25
        self.rect.centery = self.y * 50 + 25

    def draw(self, screen):
        screen.blit(self.surface, self.rect)