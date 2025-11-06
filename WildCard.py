from Card import Card
from Suit import Suit

class WildCard(Card):
    def __init__(self, rang: str | int):
        super().__init__(rang, Suit.WILD)

    def __str__(self):
        return "Wild " + super().__str__()