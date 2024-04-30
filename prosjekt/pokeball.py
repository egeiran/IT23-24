import pygame

import constants as c

class Pokeball(pygame.sprite.Sprite):
    def __init__(self, center: tuple, throwed: bool = False, velx: float = 0, vely: float = 0) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale_by(pygame.image.load("images/pokeball.png").convert_alpha(), 0.015)
        # pokeballsheet = pygame.image.load("images/pokeballs.png").convert_alpha()

        self.rect = self.image.get_rect(center = center)
        self.throwed = throwed
        self.velx = velx
        self.vely = vely

    def update(self):
        self.rect.centerx += self.velx
        self.rect.centery += self.vely
        self.vely += c.acc_y


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)