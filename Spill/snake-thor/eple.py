from figur import Figur
import random
from konstanter import *


class Eple(Figur):
    def __init__(self) -> None:
        x = random.randint(0, ANTALL_KOLONNER)
        y = random.randint(0, ANTALL_RADER)
        super().__init__(x, y, "red")