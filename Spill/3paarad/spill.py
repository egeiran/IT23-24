import pygame as pg
from spillebrett import Spillebrett

# Oppsett av pygame
pg.init()
BREDDE = 600 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pg.display.set_mode((BREDDE, HOYDE))
klokke = pg.time.Clock()
kjorer = True
farge = "red"
brett = Spillebrett(farge)

 
# OPPSETT AV SPILL HER:
vunnet = False

while kjorer:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pg.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pg.QUIT:
            kjorer = False
 
 
    if vunnet == False:
        # Input fra mus:
        mus_posisjon = pg.mouse.get_pos()
        mus_klikk = pg.mouse.get_pressed()

        if mus_klikk[0]:
            i = 0
            for rute in brett.ruter:    
                if rute.rect.collidepoint(mus_posisjon):
                    if rute.farge == 0:
                        if farge == "red":
                            rute.deaktiver(1)
                            brett.rod.append(i)
                        elif farge ==  "blue":
                            rute.deaktiver(2) 
                            brett.bla.append(i)

                        if farge == "red":
                            farge =  "blue"
                        else:
                            farge = "red"
                i += 1

    if vunnet == False:
        if brett.sjekkvinn():
            if farge == "red":
                farge = "blue"
            else:
                farge = "red"
            vunnet = True
    else:
        vindu.fill(farge)
    # Oppdater spill her:
    # Tegn på skjermen her:
    brett.tegn(farge, vindu)
 
    # flip() oppdater vinduet med alle endringer
    pg.display.flip()
 
    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60) 

 
pg.quit()

