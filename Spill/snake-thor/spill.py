import pygame
from spiller import Spiller
from eple import Eple
from konstanter import *
 
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
spiller = Spiller()
epler = [Eple()]
teller = FPS *  TID_MELLOM_EPLER

while True:
    # fyller skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    spiller.håndter_tastetrykk(taster)
 
    # Oppdater spill her:
    spiller.flytt()
    kollisjonseple = spiller.sjekk_kollisjon(epler)
    if kollisjonseple:
        epler.remove(kollisjonseple)
        epler.append(Eple())
        spiller.spis_eple()

    # Nye epler hvert TID_MELLOM_EPLER sekund
    teller -= 1
    if teller < 0:
        epler.append(Eple())
        teller = FPS * TID_MELLOM_EPLER
 
    # Tegn på skjermen her:
    spiller.tegn(vindu)
    for eple in epler:
        eple.tegn(vindu)
 
    pygame.display.flip()
    klokke.tick(FPS) 
 