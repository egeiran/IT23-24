def er_primtall(tall):    # definerer en funksjon
    for i in range(tall): # lager en for løkke som går like mange ganger som verdien til tall - BURDE STARTE PÅ 1 FOR Å IKKE DELE PÅ 0
        if tall % i == 0: # sjekker om du får en rest dersom du deler tall på i 
            return True   # returnerer True dersom tallet er delelig på noe VIL ALLTID RETURNERE TRUE, PGA LØKKEN STARTER PÅ 1
    return False          # returnerer False dersom den ikke returnerte True i løkken

"""
Mulig jeg har gjort helt feil her, men sånn jeg endte opp med å få det
gjør at koden aldri vil returnere False siden siden for løkken starter
med å dele på 1, noe som alltid vil resultere i 0 i rest. 
Den vil heller ikke funke, siden en slik fordi løkken vil starte på 0
og vil dermed få en feilmelding dersom du ikke skriver 
(1 (eller annet tall),tall), noe jeg har gjort på neste for å få til 
å funke.
"""

def er_faktisk_primtall(tall):
    for i in range(2, tall):    # starter på 2 slik at det ikke kommer feilmelding, og ikke 1 siden alt kan deles på 1
        if tall % i == 0:       
            return False        # returnerer False dersom den er delelig
    return True                 # returnerer True dersom den ikke er delelig