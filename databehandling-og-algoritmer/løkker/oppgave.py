with open("basics.txt", "r") as fil:
    data = fil.read()

handleLISTE = data.split("\n")
print(handleLISTE)

handel = "heihei"
while handel != "":
    print("Hva vil du kjøpe? Dersom handlelisten er ferdig kan du trykke Enter.")
    handel = input("> ")
    if handel != "":
        handleLISTE.append(handel.title())

with open("handleliste.txt", "w") as fil:
    for linje in handleLISTE:
        fil.write(f"{linje} \n")