import pygame

class Pokeball(pygame.sprite.Sprite):
    def __init__(self, center: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale_by(pygame.image.load("images/pokeball.png").convert_alpha(), 0.015)
        self.width = self.image.get_width()
        self.rect = (center[0] - self.width / 2, center[1], self.width, self.width)

    def picked_up(self):
        print("picked up")
        self.kill()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)