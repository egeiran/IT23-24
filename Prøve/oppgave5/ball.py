import pygame
import random
import math

from objekt import Objekt

class Ball(Objekt):
    def __init__(self, x=(1200 - 10) / 2, y=(800 - 10) / 2) -> None:
        self.x = x
        self.y = y
        self.width = 10
        self.rect: pygame.rect.Rect = pygame.rect.Rect(self.x, self.y, self.width, self.width)
        super().__init__(self.rect)
        self.vel = 10

        self.vel_x = random.randint(-5, 5)
        if self.vel_x == 0:
            self.vel_x = 3
        elif abs(self.vel_x) < 2:
            self.vel_x = self.vel_x/self.vel_x * 2
        self.vel_y = math.sqrt(self.vel**2 - self.vel_x**2)
    
    def update(self):
        self.rect.top += self.vel_y
        self.rect.left += self.vel_x