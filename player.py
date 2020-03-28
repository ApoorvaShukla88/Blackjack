import random
import Hand
import Dealer


class Player(Hand, Dealer):

    def __init__(self, player_cards):
        self.player_cards = []


    def no_of_cards_in_hand(self):
        while len(self.player_cards) != 2:
            self.player_cards.append(random.randint(1,11))
        if len(self.player_cards) == 2:
            print("You Have "+ self.player_cards)

    def player_hand(self):
        while sum(self.player_cards) < 21:
            player_action = str(input("Do you want HIT or STAY "))
        if player_action == 'HIT':
            self.player_cards.append((random.randint(1,11)))
            print("Now Player has "+ str(sum(self.player_cards) + "with these cards" + self.player_cards))
        else:
            print("You have "+ str(sum(self.player_cards) + "with these cards" + self.player_cards))


    def result(self):
        if str(sum(self.dealer_cards) > str(sum(self.player_cards):
            print("Dealer WIN")
        else:
            print("Player WIN")