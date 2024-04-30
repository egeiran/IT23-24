import pygame
import random

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, pokemon: str, block_group: pygame.sprite.Group) -> None:
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load(f"images/{pokemon}.png").convert_alpha(), 0.4)
        self.rect = self.image.get_rect()
        self.index = random.randint(0,len(block_group) - 1)
        self.rect.bottom = list(block_group)[self.index].standheight - 10
        self.rect.centerx = list(block_group)[self.index].rect.centerx
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)