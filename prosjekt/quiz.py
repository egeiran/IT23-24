print("-- Velkommen til Quiz --")

print("")
print("Quizzen har 5 spørsmål. Klarer du alle?")
print("")

utfall = True

svaraltb = "abcd"

spørsmål = [
    {
        "spm": "Hva er første pokemonen i pokedexen?",
        "svaralt": ["Bulbasaur", "Squirtle", "Charmander", "Pikachu"],
        "r": "a"
    },
    {
        "spm": "Hvor er OL 2024?",
        "svaralt": ["Oslo", "Paris", "Texas", "Tokyo"],
        "r": "b"
    },
    {
        "spm": "Når er bursdagen til Hanken?",
        "svaralt": ["12. September", "18. Januar", "28. April", "21. Juli"],
        "r": "d"
    }
]

nr = 1
while utfall == True and nr < 4:
    print(f'Spørsmål {nr}: {spørsmål[nr-1]["spm"]}')
    for i in range(4):
        print(f'{svaraltb[i]}: {spørsmål[nr-1]["svaralt"][i]}')
    svar = input("Svar: ")
    if svar != spørsmål[nr-1]["r"]:
        utfall = False
    nr += 1
    print()

print("----------------------------------------------------------")
print()
if utfall == True:
    print("Gratulerer, du vant!!")
else:
    print("Du tapte din nøøørd")