import os
import sys
import json
from pokemon import Pokemon
from trener import Trener

with open("pokemon.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

def rens_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

pokemon_liste = []
for pokemon_ordbok in data:
    ny_pokemon = Pokemon(pokemon_ordbok)
    pokemon_liste.append(ny_pokemon)

trenerliste = []


while True:
    rens_terminal()
    print("-- Velkommen til Pokémon --")
    print("1. Se pokémonoversikt")
    print("2. Se treneroversikt")
    print("3. Lag trener")
    print("4. Avslutt")
    brukerinput = input("> ")

    if brukerinput == "1":
        rens_terminal()
        print("Pokémonoversikt")
        for pokemon in pokemon_liste:
            print(pokemon)

    elif brukerinput == "2":
        rens_terminal()
        print("Treneroversikt")
        for trener in trenerliste:
             print(trener)
        input("Trykk enter for å gå tilbake til menyen")

    elif brukerinput == "3":
            rens_terminal()
            print("Lager ny trener")

            print("")
            print("Hva heter treneren?")
            trenernavn = input("> ")
            trenerliste.append(Trener(trenernavn))



        
    