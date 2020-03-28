from random import random
import Hand


class Dealer(Hand):

    def __init__(self,dealer_cards):
        self.dealer_cards = []

    def no_of_cards_in_hand(self):
        while len(self.dealer_cards) != 2:
            self.dealer_cards.append(random.randint(1, 11))
        if len(self.dealer_cards) == 2:
            print("Dealer has X and " + self.dealer_cards[1])

    def dealer_hand(self):
        if sum(self.dealer_cards) == 21:
            print("Dealer has 21 and Win")
        elif sum(self.dealer_cards) > 21:
            print("Dealer has Busted")
