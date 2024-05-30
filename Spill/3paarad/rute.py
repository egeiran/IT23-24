import pygame as pg
class Rute:
    def __init__(self, x, y) -> None:
        self.surface: pg.Surface = pg.Surface((95, 95))
        self.rect = self.surface.get_rect()
        self.surface.fill("white")
        self.rect.topleft = (x,y)
        self.farge = 0

    def tegn(self, surface):
        surface.blit(self.surface, self.rect)
    
    def deaktiver(self, spiller: int):
        self.farge = spiller
        if spiller == 1:
            self.surface.fill("red")
        elif spiller == 2:
            self.surface.fill("blue")


        