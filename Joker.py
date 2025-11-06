from typing import Callable

class Joker:
    def __init__(self, chips: int, mult: int, action: Callable[[int, int], (int, int)] = None):
        self.__chips = chips
        self.__mult = mult
        self.__action = action

    @property
    def chips(self):
        return self.__chips

    @property
    def mult(self):
        return self.__mult

    @property
    def action(self):
        return self.__action
