from random import random

from Blackjack import deck
from Blackjack.deck import Deck
from Blackjack.player import Player






def main():

    dealer = Player()
    player1 = Player()
    deck1 = Deck()

    deck1.reset()

    player1.hand_cards.clear()
    player1.choice = ""

    dealer.hand_cards.clear()
    dealer.choice = ""

    player1.hand_cards.append(deck1.draw_card())
    dealer.hand_cards.append(deck1.draw_card())

    def player1_hand(self):
        while sum(self.player1.hand_cards) < 21:
            player_action = str(input("Do you want HIT or STAY "))
        if player_action == 'HIT':
            self.player1.hand_cards.append((random.randint(1, 11)))
            print("Now Player has " + str(sum(self.player1.hand_cards) + "with these cards" + self.player1.hand_cards))
        else:
            print("You have " + str(sum(self.player1.hand_cards) + "with these cards" + self.player1.hand_cards))



























def result(self):
    if str(sum(self.dealer_cards) > str(sum(self.player_cards):
        print("Dealer WIN")
    else:
        print("Player WIN")

        # from random import random
        # import Hand
        #
        # class Dealer(Hand):
        #
        #     def __init__(self, dealer_cards):
        #         self.dealer_cards = []
        #
        #     def no_of_cards_in_hand(self):
        #         while len(self.dealer_cards) != 2:
        #             self.dealer_cards.append(random.randint(1, 11))
        #         if len(self.dealer_cards) == 2:
        #             print("Dealer has X and " + self.dealer_cards[1])
        #
        #     def dealer_hand(self):
        #         if sum(self.dealer_cards) == 21:
        #             print("Dealer has 21 and Win")
        #         elif sum(self.dealer_cards) > 21:
        #             print("Dealer has Busted")
