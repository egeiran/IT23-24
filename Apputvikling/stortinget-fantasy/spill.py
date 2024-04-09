import os
import sys
import time
import json

from politiker import Politiker

def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# 1. Oppsett
with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

representanter = data["dagensrepresentanter_liste"]

# Oppretter en liste med politiker-objekter ( objekter av klassen politiker )
politikere = []
for representant in representanter:
    politikere.append(Politiker(representant))

rens_terminal()

print(" -- Velkommen til Stortinget-fantasy --")
input()

rens_terminal()
for i in range(4):
    print("."*(i))
    time.sleep(0.2)
    rens_terminal()

while True:
    rens_terminal()
    print(" -- Stortinget-fantasy --")
    print("")

    print("1: Vis politikeroversikt")
    print("2: Avslutt")
    brukervalg = input(" > ")

    if brukervalg == "1":
        print("politikeroversikt")
        for politiker in politikere:
            print(politiker)
        print(len(politikere))
        input("Trykk enter for å gå tilbake til hovedmenyen. \n")
    elif brukervalg == "2":
        for i in range(4):
            rens_terminal()
            print("Avslutter", "."*i, sep="")
            time.sleep(0.2)
        break
    else:
        print("Ugyldig input.")
        input("Trykk enter for å gå tilbake til hovedmenyen \n")

rens_terminal()
print("Takk for nå")