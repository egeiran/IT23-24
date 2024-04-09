import json
import time
import sys
import os
from pokemon import Pokemon

def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

with open("pokemon.json", "r") as fil:
    data = json.load(fil)

pokemen = []
for pokemon in data:
    pokemen.append(Pokemon(pokemon))

print(" -- Velkommen til Pokemon -- ")
time.sleep(1)

while True:
    rens_terminal()
    print(" -- Pokemon er dritdope -- ")

    print("1: Se alle pokemon")
    print("2: Velg en pokemon du vil se (basert på pokedex nummeret deres)")
    print("3: Avslutt programmet")
    brukervalg = input(" > ")
    if brukervalg == "1":
        for pokemon in pokemen:
            print(pokemon)
    elif brukervalg == "2":
        print("Skriv pokedexnummeret til pokemonen du vil se")
        pokeindex = -1
        while pokeindex <= 0 or pokeindex > 151:
            pokeindex = int(input(" > "))
            if pokeindex <= 0 or pokeindex > 151:
                print("Du må velge et tall mellom 1 og 151")
        print(pokemen[pokeindex-1])
    else:
        print("Avslutter...")
        break
    input("")