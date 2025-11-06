from Suit import Suit

class Card:
    COLORS = {
        Suit.CLUBS: "♣",
        Suit.DIAMONDS: "♦",
        Suit.SPADES: "♠",
        Suit.HEARTS: "♥",
        Suit.WILD: "W"
    }

    RANGS = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11
    }

    def __init__(self, rang: str | int, suit: Suit):
        if rang not in Card.RANGS:
            raise ValueError(f"Invalid card rank: {rang}")

        self._rank = rang
        self._suit = suit
        self._chips = Card.RANGS[rang]

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def chips(self):
        return self._chips

    def __eq__(self, other: Card):
        return self._rank == other._rank and self._suit == other._suit

    def __str__(self):
        return str(self._rank) + Card.COLORS[self._suit]
