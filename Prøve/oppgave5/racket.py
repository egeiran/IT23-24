import pygame

from objekt import Objekt

class Racket(Objekt):
    def __init__(self, left: bool) -> None:
        self.width = 12
        self.height = 80
        self.y = (800 - self.height) / 2
        if left == True:
            self.x = 15
            self.rect: pygame.rect.Rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        else: 
            self.x = 1200 - 15 - 12
            self.rect: pygame.rect.Rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        super().__init__(self.rect)
        self.score = 0
        self.left = left


    def flytt(self, direction: int = 0):
        self.rect.top += direction * 6