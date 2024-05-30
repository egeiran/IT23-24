import pygame as pg
from rute import Rute

class Spillebrett: 
    def __init__(self, farge) -> None:
        self.ruter: list[Rute] = []
        for i in range(1,4): #setter y
            for y in range(1,4): #setter x for hver y
                self.ruter.append(Rute(y*100 + 50, i*100 + 50))
                print(f"{y},{i}")
        self.bakgrunn = farge

        self.spillersurface: pg.Surface = pg.Surface((400, 400))
        self.spillerrect = self.spillersurface.get_rect()
        self.spillersurface.fill(farge)
        self.spillerrect.topleft = (100,100)

        self.bgsurface: pg.Surface = pg.Surface((390, 390))
        self.bgrect = self.bgsurface.get_rect()
        self.bgsurface.fill("black")
        self.bgrect.topleft = (105,105)

        self.rod = []
        self.bla = []
        self.vinn = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]



    def tegn(self, farge, surface: pg.Surface):
        self.spillersurface.fill(farge)
        surface.blit(self.spillersurface, self.spillerrect)
        surface.blit(self.bgsurface, self.bgrect)

        for rute in self.ruter:
            rute.tegn(surface)
    
    def sjekkvinn(self):
        vinn_rod = 0
        vinn_bla = 0
        for list in self.vinn:
            for object in list:
                if object in self.rod:
                    vinn_rod +=1
                elif object in self.bla:
                    vinn_bla +=1

            if vinn_rod == 3:
                break
            elif vinn_bla == 3:
                break
            else: 
                vinn_rod = 0
                vinn_bla = 0
        if vinn_rod == 3:
            return True


        elif vinn_bla == 3:
            return True


