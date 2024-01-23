# ALGORITME 1

def høyeste(liste: list[int]):
    print(liste)
    høyest = liste[0]
    for tall in liste:
        if tall > høyest:
            høyest = tall
    return høyest

def nest_høyeste(liste: list[int]):
    høyest = [liste[0], liste[1]]
    for i in range(2, len(liste)):
        if liste[i] > min(høyest):
            høyest[0] = liste[i]
            høyest.sort()
    return høyest[0]

def n_høyeste_egen(liste: list[int], n: int):
    liste.sort(reverse=True)
    return liste[:n]

def n_høyeste(liste: list[int], n: int):
    høyeste_n = []
    for i in range(n):
        høyest = høyeste(liste)
        liste.remove(høyest)
        høyeste_n.append(høyest)
    return høyeste_n