from konstanter import *
from figur import Figur

class Kroppsdel(Figur):
    def __init__(self, x: int, y: int, x_fart: int, y_fart: int, farge: str) -> None:
        super().__init__(x, y, farge)
        self.x_fart = x_fart
        self.y_fart = y_fart
    
    def flytt(self, x: int, y: int):
        self.x = x
        self.y = y
        if self.x > ANTALL_KOLONNER:
            self.x = 0
        if self.x < 0:
            self.x = ANTALL_KOLONNER
        if self.y > ANTALL_RADER:
            self.y = 0
        if self.y < 0:
            self.y = ANTALL_RADER
        self.oppdater_rect()

    
    def oppdater_fart(self, x_fart: int, y_fart: int):
        self.x_fart =  x_fart
        self.y_fart =  y_fart
    
    def ny_kroppsdel(self):
        ny_x = self.x - self.x_fart
        ny_y = self.y - self.y_fart
        return Kroppsdel(ny_x, ny_y, self.x_fart, self.y_fart, "lightgreen")