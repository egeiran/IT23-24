import json
import time
import os
import sys

# KLASSER

class Aktivitet:
    def __init__(self, navn: str, alle: int, menn: int, kvinner: int) -> None:
        self.navn = navn
        self.alle = alle
        self.menn = menn
        self.ordbok = {
            "Alle": alle,
            "Menn": menn,
            "Kvinner": kvinner
        }
        self.kvinner = kvinner
    
    def __str__(self) -> str:
        # Endrer hvordan en klasse printes
        return f"{self.navn}: \n  (Alle: {self.alle}, Menn: {self.menn}, Kvinner: {self.kvinner})"

    def __repr__(self) -> str:
        # Endrer hvordan en klasse vises i en liste
        return self.__str__()

class Hovedaktivitet(Aktivitet):
    def __init__(self, navn: str, alle: int, menn: int, kvinner: int) -> None:
        super().__init__(navn, alle, menn, kvinner)
        self.underaktiviteter: list[Underaktivitet] = []

    def sorter_underaktiviteter(self):
        return sorted(self.underaktiviteter, key=lambda akt: akt.alle, reverse=True)

    def __str__(self) -> str:
        return "\nH: " + super().__str__() + "{}".format(' '.join(underaktivitet.__str__() for underaktivitet in self.underaktiviteter))

class Underaktivitet(Aktivitet):
    def __init__(self, navn: str, alle: int, menn: int, kvinner: int) -> None:
        super().__init__(navn, alle, menn, kvinner)
    
    def __str__(self) -> str:
        return "\n  U: " + super().__str__()

# FUNKSJONER

def Sorter_Aktiviteter(liste, kjønn):
    """
        Sorterer en liste med aktiviteter basert på kjønn og tiden de bruker på det
    """
    kjønnet = kjønn.title()
    if kjønnet == "Alle":
        ny_liste = sorted(liste, key= lambda aktivitet:aktivitet.alle, reverse=True)
    elif kjønnet == "Menn":
        ny_liste = sorted(liste, key= lambda aktivitet:aktivitet.menn, reverse=True)
    elif kjønnet == "Kvinner":
        ny_liste = sorted(liste, key= lambda aktivitet:aktivitet.kvinner, reverse=True)
    return ny_liste

def Sorter_Alle_Underaktiviteter(liste, kjønn):
    underaktiviteter = []
    for hovedakt in liste:
        for underakt in hovedakt.underaktiviteter:
            underaktiviteter.append(underakt)
    ny_liste = sorted(underaktiviteter, key=lambda underakt:underakt.ordbok[kjønn], reverse=True)
    return ny_liste

def timer_og_min_til_minutter(timer_min):
    timer_s, minutter_s = str(float(timer_min)).split(".")
    return int(timer_s) * 60 + int(minutter_s)

def vent():
    for i in range(4):
        print("."*(i))
        time.sleep(0.2)
        rens_terminal()

def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

with open("datasett.json", "r", encoding="utf-8") as f:
    data = json.load(f)

hovedaktiviteter = []

for i in range(0, len(data), 3):
    navn = data[i]["alle aktiviteter"]
    alle = data[i]["Tidsbruk 2000 I alt"]
    menn = data[i + 1]["Tidsbruk 2000 I alt"]
    kvinner = data[i + 2]["Tidsbruk 2000 I alt"]
    if "� " not in data[i]["alle aktiviteter"]:
        hovedaktiviteter.append(Hovedaktivitet(navn, alle, menn, kvinner))
    else:
        navn = navn.replace("� ", "")
        hovedaktiviteter[-1].underaktiviteter.append(Underaktivitet(navn, alle, menn, kvinner))

while True:
    rens_terminal()
    print(f"-- Hovedvalg --")
    print()
    print("1: Til hovedaktivitetsoversikt")
    print("2: Alle underaktiviteter sortert")
    print("3: Alle hovedaktiviteter sortert")
    print("a: Avslutt")
    print()
    valg = input("> ")
    rens_terminal()
    if valg == "1": 
        print(f"-- Hvilken hovedaktivitet vil du ha? (1 til {len(hovedaktiviteter)}) --")
        print()
        for i in range(len(hovedaktiviteter)):
            print(f"{i + 1}: {hovedaktiviteter[i].navn} ({len(hovedaktiviteter[i].underaktiviteter)} underaktiviteter)")
        print()
        valg = input("> ")
        rens_terminal()
        input(hovedaktiviteter[int(valg) - 1])
    elif valg == "2":
        for aktivitet in Sorter_Alle_Underaktiviteter(hovedaktiviteter, "Alle"):
            print(aktivitet)
        input("Trykk enter for å gå videre")
        vent()
    elif valg == "3":
        print()
        print("Hvilket kjønn vil du sortere etter (Alle, Menn, Kvinner)")
        kjønn = input("> ").title()
        print()
        sortert_aktiviteter = Sorter_Aktiviteter(hovedaktiviteter, kjønn)
        for i in range(len(sortert_aktiviteter)):
            print(i + 1, sortert_aktiviteter[i].navn, f"({sortert_aktiviteter[i].ordbok[kjønn]})")
        input("Trykk enter for å gå videre")
        vent()
    elif valg == "a":
        print()
        input("Avslutter")
        time.sleep(0.4)
        vent()
        break
    else:
        print("Ugyldig valg.")
        time.sleep(0.5)
        vent()