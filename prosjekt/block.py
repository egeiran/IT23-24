import pygame
import constants as c

class Block():
    def __init__(self, image, rect, standable: bool) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect: pygame.rect.Rect = rect
        self.standheight = rect[1] + 5
        self.standable = standable

    def draw(self, screen):
        screen.blit(self.image, self.rect)
