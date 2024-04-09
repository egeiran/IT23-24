import os
import sys
import json
from politiker import Politiker
from fantasyparti import Fantasyparti

def rens_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"]

politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)

print("-- Velkommen til Stortinget-fantasy --")

print()
print("Du må stifte parti for å spille spillet.")
print("Hva skal ditt parti hete?")
partinavn = input("> ")
print("Hva heter du?")
eier = input("> ")
spillerparti = Fantasyparti(partinavn, eier)
print(f"Gratulerer! Det nye partiet {partinavn} ble stiftet av {eier}.")
input("Trykk enter for å starte spillet")

while True:
    rens_terminal()
    print("-- Stortinget-fantasy --")
    print("1: Vis politiker oversikt")
    print("2: Mitt Parti")
    print("3: Avslutt")
    brukervalg = input("> ")

    if brukervalg == "1":
        print("Politiker overskrift")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å for å gå tilbake til hovedmenyen")

    elif brukervalg == "2":
        rens_terminal
        print("Mitt parti")
        spillerparti.vis_parti()
        input("Trykk enter for å gå tilbake til menyen")


    elif brukervalg == "3":
        print("Avslutter...")
        break
    else:
        print("Ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmeny")

print("Takk for nå")