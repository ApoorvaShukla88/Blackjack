from random import random


class Deck:

    def __init__(self,):
        self.cards = []


    def shuffle(self):
      random.shuffle(self.cards)


    def draw_card(self):
