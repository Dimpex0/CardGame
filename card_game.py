from enum import Enum
from typing import Callable
from collections import defaultdict

class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
    WILD = 5

class Card:
    COLORS = {
        Suit.CLUBS: "♣",
        Suit.DIAMONDS: "♦",
        Suit.SPADES: "♠",
        Suit.HEARTS: "♥",
        Suit.WILD: "W"
    }

    RANKS = {
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
        if rang not in Card.RANKS:
            raise ValueError(f"Invalid card rank: {rang}")

        self._rank = rang
        self._suit = suit
        self._chips = Card.RANKS[rang]

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def chips(self):
        return self._chips

    def __str__(self):
        return str(self._rank) + Card.COLORS[self._suit]

class SilverCard(Card):
    def __init__(self, rang: str | int, color: Suit):
        super().__init__(rang, color)
        self._chips *= 2

    def __str__(self):
        return "Silver " + super().__str__()

class GoldCard(Card):
    def __init__(self, rang: str | int, color: Suit):
        super().__init__(rang, color)
        self._chips *= 4

    def __str__(self):
        return "Gold " + super().__str__()

class WildCard(Card):
    def __init__(self, rang: str | int):
        super().__init__(rang, Suit.WILD)

    def __str__(self):
        return "Wild " + super().__str__()

class Joker:
    def __init__(self, chips: int, mult: int, action = None):
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

def score(cards: list[Card], jokers: list[Joker]) -> int:
    if len(cards) < 5:
        return 0

    ranks = defaultdict(int)
    suits = defaultdict(int)
    for card in cards:
        ranks[card.rank] += 1

    wild_cards_count = 0
    for card in cards:
        if card.suit == Suit.WILD:
            wild_cards_count += 1
        else:
            suits[card.suit] += 1

    if wild_cards_count:
        for suit in suits:
            suits[suit] += wild_cards_count

    additional_ranks = sum([value for value in ranks.values() if value > 1])
    additional_suits = sum([value for value in suits.values() if value > 1])

    cards_chips = sum([card.chips for card in cards])
    jokers_chips = sum([joker.chips for joker in jokers])
    total_chips = cards_chips + jokers_chips
    jokers_multiplicator = sum([joker.mult for joker in jokers]) + 1
    jokers_multiplicator += additional_ranks + additional_suits

    for joker in jokers:
        if joker.action is not None:
            total_chips, jokers_multiplicator = joker.action(total_chips, jokers_multiplicator)

    return total_chips * jokers_multiplicator