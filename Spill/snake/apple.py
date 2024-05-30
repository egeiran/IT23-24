from figure import Figure
import random

class Apple(Figure):
    def __init__(self, apples, snakebody) -> None:
        while True:
            cont = True
            self.x = random.randint(0,12)
            self.y = random.randint(0,12)
            for apple in apples:
                if self.x == apple.x and self.y == apple.y:
                    cont = False
            for bodypart in snakebody:
                if self.x == bodypart.x and self.y == bodypart.y:
                    cont = False
            if cont:
                break

        super().__init__(self.x, self.y, (255,0,0))