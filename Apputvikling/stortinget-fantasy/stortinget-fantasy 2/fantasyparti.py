from politiker import Politiker

class Fantasyparti:
    def __init__(self, navn: str, eier: str) -> None:
        self.navn: str = navn
        self.eier: str = eier
        self.poeng: int = 0
        self.saldo: int = 100_000
        self.partileder: Politiker = None
        self.politikere: list[Politiker] = []

    def __str__(self) -> str:
        return f"{self.navn} - {self.eier} ({self.poeng} poeng, {self.saldo} kr)"

    def kjøp_politiker(self, politiker: Politiker):
        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.saldo -= politiker.verdi
            self.politikere.append(politiker)
        else:
            print("FEIL!")

    def selg_politiker(self, politiker: Politiker):
        if politiker in self.politikere:
            self.saldo += politiker.verdi
            self.politikere.remove(politiker)
        else: 
            print("Denne politikeren er ikke i ditt parti")

    def vis_parti(self):
        print(f"-- {self.navn} --")
        print(f"Poeng: {self.poeng}")
        print(f"Saldo: {self.saldo}")
        print("Medlemmer")
        for politiker in self.politikere:
            print(politiker)
        

if __name__ == "__main__":
    print("Tester Fantasyparti-klassen")
    testparti = Fantasyparti("Glee", "Thomas")
    print(testparti)