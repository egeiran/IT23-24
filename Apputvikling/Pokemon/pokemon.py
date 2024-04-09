class Pokemon:
    def __init__(self, pokeinfo: dict) -> None:
        self.index: int = pokeinfo["id"]
        self.name: str = pokeinfo["name"]["english"]
        self.type: list[str] = pokeinfo["type"]
        self.typestr = str(self.type).replace("'", "")[1:-1]
        self.basestats: dict = pokeinfo["base"]
        self.HP: int = self.basestats["HP"]
        self.Attack: int = self.basestats["Attack"]
        self.Defense: int = self.basestats["Defense"]
        self.Sp_Attack: int = self.basestats["Sp. Attack"]
        self.Sp_Defense: int = self.basestats["Sp. Defense"]
        self.Speed: int = self.basestats["Speed"]

    def __str__(self):
        if self.name[-1] == "s" or self.name[-1] == "z" or self.name[-1] == "x":
            name_s = self.name
        else:
            name_s = self.name+"s"
        return f'{name_s} {"type is" if len(self.type) == 1 else "types are"} {self.typestr.replace(",", " and")}'

if __name__ == "__main__":
    bulbasaur = Pokemon({
      "id": 1,
      "name": {
        "english": "Bulbasaur",
        "japanese": "フシギダネ",
        "chinese": "妙蛙种子",
        "french": "Bulbizarre"
      },
      "type": ["Grass", "Poison"],
      "base": {
        "HP": 45,
        "Attack": 49,
        "Defense": 49,
        "Sp. Attack": 65,
        "Sp. Defense": 65,
        "Speed": 45
      }
    })

    print(bulbasaur)