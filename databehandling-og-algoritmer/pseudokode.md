# Pseudokode

- en måte å beskrive en algoritme eller et program på ved hjelp av naturlig språk
- brukes ofte som et verktøy for å planlegge og designe algoritmer før de faktisk blir kodet i et bestemt programmeringsspråk
- gjør det lettere å kommunisere og samarbeide med andre programmerere, samt å teste og feilsøke algoritmer før de blir kodet.
- en god måte å lære grunnleggende programmeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og
logiske uttrykk fungerer sammen for å løse et bestemt problem.

# Eksempel: Penger tjent på spotify

> En algoritme som regner ut hvor mye vi tjener på spotify

```pseudo
Hent inn antall streams
Hvis antall streams er større enn 30 000 000
    Returner antall streams * 0.7
Ellers hvis antall streams er større enn 1 400 000
    Returner antall streams * 0.4
Ellers:
    Returner 0
```

```python
def spenn(ant_streams):
    if ant_streams > 30000000:
        return ant_streams * 0.7
    elif ant_streams > 1400000:
        return ant_streams * 0.4
    else:
        return 0
```