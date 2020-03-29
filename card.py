import random
import os

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
suits = ['Club', "Spade", "Diamond", "Hearts"]
TotalCards = 52


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 1,11
        else:
            return self.rank

    def __str__(self):
        return self.suit + ":" + self.value()

