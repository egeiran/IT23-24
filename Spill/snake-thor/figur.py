import pygame
from konstanter import *

class Figur:
    def __init__(self, x: int, y:int, farge: str) -> None:
        self.surface = pygame.Surface((CELLEBREDDE, CELLEHOYDE))
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        self.rect.left = self.x * CELLEBREDDE
        self.rect.top = self.y * CELLEHOYDE
        self.surface.fill(farge)

    def oppdater_rect(self):
        self.rect.left = self.x * CELLEBREDDE
        self.rect.top = self.y * CELLEHOYDE
    
    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)
    
    def sjekk_kollisjon(self, figurliste):
        # en metode som tar inn en liste med figurer og returnerer den første figuren som
        # kolliderer med denne figuren (self), hvis ikke den kolliderer med noen i listen
        # returnerer den None
        for figur in figurliste:
            if self.rect.colliderect(figur.rect):
                return figur
        return None
