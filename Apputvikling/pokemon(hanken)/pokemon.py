class Pokemon:
    def __init__(self, pokémon_ordbok: dict) -> None:
        self.id: str = pokémon_ordbok["id"]
        self.navn: str = pokémon_ordbok["name"]["english"]
        self.type: list = pokémon_ordbok["type"]
        self.hp: int = pokémon_ordbok["base"]["HP"]
        self.attack: int = pokémon_ordbok["base"]["Attack"]
        self.defense: int = pokémon_ordbok["base"]["Defense"]
        self.sp_attack: int = pokémon_ordbok["base"]["Sp. Attack"]
        self.sp_defense: int = pokémon_ordbok["base"]["Sp. Defense"]
        self.speed:int = pokémon_ordbok["base"]["Speed"]

    def __str__(self) -> str:
        str(self.type)[1:-1]
        return f"{self.navn} ({', '.join(self.type)})"
