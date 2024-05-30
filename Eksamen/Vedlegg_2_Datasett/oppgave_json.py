# Sletter øverste linje i JSON filen, da det ikke går an å loade json filen

"05994: Tid brukt til ulike aktiviteter en gjennomsnittsdag blant alle (timer og minutter), etter alle aktiviteter, kjønn, statistikkvariabel, år og alder"

import json

with open("datasett.json", "r", encoding="UTF-8") as f:
    data = json.load(f)

aktiviteter = {}

for aktivitet in data[3:-3]:
    if "� " not in aktivitet["alle aktiviteter"]:
        if aktivitet["alle aktiviteter"] not in aktiviteter:
            aktiviteter[aktivitet["alle aktiviteter"]] = {
                aktivitet["kjønn"]: aktivitet["Tidsbruk 2000 I alt"],
            }
        aktiviteter[aktivitet["alle aktiviteter"]][aktivitet["kjønn"]] = aktivitet["Tidsbruk 2000 I alt"]
        aktiviteten = aktivitet["alle aktiviteter"]
        aktivitetens_ordbok = False
    else:
        if aktivitetens_ordbok == False:
            aktiviteter[aktiviteten]["Underaktiviteter"] = {}
            aktivitetens_ordbok = True
        _aktivitet = aktivitet["alle aktiviteter"].replace("� ", "")
        if _aktivitet not in aktiviteter[aktiviteten]["Underaktiviteter"]:
            aktiviteter[aktiviteten]["Underaktiviteter"][_aktivitet] = {
                    aktivitet["kjønn"]: aktivitet["Tidsbruk 2000 I alt"]
                }
        if aktivitet["kjønn"] not in aktiviteter[aktiviteten]["Underaktiviteter"][_aktivitet]:
            aktiviteter[aktiviteten]["Underaktiviteter"][_aktivitet][aktivitet["kjønn"]] = aktivitet["Tidsbruk 2000 I alt"]

with open("print_datasett.json", "w") as f:
    json.dump(aktiviteter, f)
    f.close()