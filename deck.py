from random import random

from Blackjack.card import Card


class Deck():

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards.clear()
        ranks = [11, 10, 10, 10, 10, 9, 8 ,7, 6, 5, 4, 3, 2]
        suits = ["Club", "Spade", "Diamond", "Hearts"]

        for i in ranks:
            for j in suits:
                self.cards.append(Card(i, j))



    def shuffle(self):
      random.shuffle(self.cards)


    def draw_card(self):
        card = self.cards.pop()
        return card


