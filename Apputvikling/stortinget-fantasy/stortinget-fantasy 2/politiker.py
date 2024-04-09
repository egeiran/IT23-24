class Politiker:
    def __init__(self, politker_ordbok: dict):
        self.fornavn: str = politker_ordbok["fornavn"]
        self.etternavn: str = politker_ordbok["etternavn"]
        self.parti: str = politker_ordbok["parti"]["navn"]
        self.fylke: str = politker_ordbok["fylke"]["navn"]
        self.kjønn: str = "kvinne" if politker_ordbok["kjoenn"] == 1 else "mann"
        self.komiteer: list[str] = [komite["navn"] for komite in politker_ordbok["komiteer_liste"]]
        self.verdi: int = 1000
        self.ukepoeng: list[int] = []

    def __str__(self):
        # spesille-metode som bestemmer hvordan en politker skal printes
        return f"{self.fornavn} {self.etternavn} ({self.parti})"

if __name__ == "__main__":
    print("Tester Politker-klassen")
