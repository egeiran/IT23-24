from figure import Figure

class Bodypart(Figure):
    def __init__(self, x, y, color=(0,0,200)) -> None:
        super().__init__(x, y, color)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"