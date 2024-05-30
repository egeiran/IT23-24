import pygame
from konstanter import *
from kroppsdel import Kroppsdel


class Spiller:
    def __init__(self) -> None:
        self.x_fart = 1
        self.y_fart = 0
        x = ANTALL_KOLONNER // 2 # bruker heltallsdivisjon // for at x skal bli et heltall
        y = ANTALL_RADER // 2 
        hode = Kroppsdel(x, y, self.x_fart, self.y_fart, "green")
        self.kropp = [hode]

    def sjekk_kollisjon(self, figurliste):
        return self.kropp[0].sjekk_kollisjon(figurliste)
    
    def spis_eple(self):
        siste_del = self.kropp[-1]
        ny_del = siste_del.ny_kroppsdel()
        self.kropp.append(ny_del)
    
    def flytt(self):
        # går gjennom kroppen baklengs fra siste til nest første (tar ikke med hodet)
        for i in range(len(self.kropp) - 1, 0, -1):
            denne = self.kropp[i]
            neste = self.kropp[i - 1]
            denne.flytt(neste.x, neste.y)
            neste.oppdater_fart(neste.x_fart, neste.y_fart)

        # oppdaterer hodet for seg selv, fordi den først skal flyttes, så oppdateres med hele spillerens fart
        hode = self.kropp[0]
        hode.flytt(hode.x + hode.x_fart, hode.y + hode.y_fart)
        hode.oppdater_fart(self.x_fart, self.y_fart)
        

    def håndter_tastetrykk(self, taster):
        if taster[pygame.K_UP]:
            self.x_fart = 0
            self.y_fart = -1
        if taster[pygame.K_DOWN]:
            self.x_fart = 0
            self.y_fart = 1
        if taster[pygame.K_LEFT]:
            self.x_fart = -1
            self.y_fart = 0  
        if taster[pygame.K_RIGHT]:
            self.x_fart = 1
            self.y_fart = 0


    def tegn(self, surface):
        for kroppsdel in self.kropp:
            kroppsdel.tegn(surface)
