from Card import Card
from Suit import Suit

class GoldCard(Card):
    def __init__(self, rang: str | int, color: Suit):
        super().__init__(rang, color)
        self._chips *= 4

    def __str__(self):
        return "Gold " + super().__str__()