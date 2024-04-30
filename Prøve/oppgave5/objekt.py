import pygame

class Objekt():
    def __init__(self, rect: pygame.rect.Rect) -> None:
        self.rect:pygame.rect.Rect = pygame.rect.Rect(rect)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        