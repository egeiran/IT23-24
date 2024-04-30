import pygame
import constants as c

class Block(pygame.sprite.Sprite):
    def __init__(self, image, left, top, standable: bool) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(left=left, top=top)
        self.standheight = self.rect.top + 5
        self.standable = standable
