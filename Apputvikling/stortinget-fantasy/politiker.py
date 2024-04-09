class Politiker():
    def __init__(self, politiker_ordbok: dict) -> None:
        self.fornavn: str = politiker_ordbok["fornavn"]
        self.etternavn: str = politiker_ordbok["etternavn"]
        self.parti: str = politiker_ordbok["parti"]["navn"]
        self.fylke: str = politiker_ordbok["fylke"]["navn"]
        self.kjønn: str = "kvinne" if politiker_ordbok["kjoenn"] == 1 else "mann"
        self.komiteer: list[str] = [komite["navn"] for komite in politiker_ordbok["komiteer_liste"]]
        self.verdi: int = 1000
    
    def __str__(self):
        return f'{self.fornavn} {self.etternavn} ({self.parti})'

if __name__ == "__main__":
    print("Test")