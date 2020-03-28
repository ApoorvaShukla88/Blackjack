from random import random

from Blackjack import deck
from Blackjack.deck import Deck
from Blackjack.player import Player


def player1_hand(player1, deck1):
    while True:
        if player1.total_points() < 21:
            player_action = str(input("Do you want HIT or STAY "))
            if player_action == 'HIT':
                player1.hand_cards.append((deck1.draw_card()))
                print("Now Player has " + player1.show_hand() + " with these cards" + str(player1.show_hand()))
            elif player_action == "STAY":
                print("You have " + player1.show_hand() + " with these cards" + str(player1.show_hand()))
                return
        elif player1.total_points() > 21:
            print("Player1 Busted")
            exit(0)
        elif player1.total_points() == 21:
            print("Player1 Won")
            exit(0)


def dealer_hand(dealer, deck1):
    while True:
        if dealer.total_points() > 21:
            print("Dealer Busted")
            exit(0)
        elif dealer.total_points() < 21:
            if dealer.total_points() > 17:
                print("Dealer cant draw anymore card :" + dealer.show_hand())
                return
            else:
                dealer.hand_cards.append((deck1.draw_card()))
                print("Now Dealer has " + dealer.show_hand() + " with these cards" + dealer.show_hand())




def result(dealer, player1):
    if dealer.total_points() > player1.total_points():
        print("Dealer WIN")
    else:
        print("Player1 WIN")


def main():
    dealer = Player()
    player1 = Player()
    deck1 = Deck()

    deck1.reset()
    deck1.shuffle()

    player1.hand_cards.clear()
    player1.choice = ""

    dealer.hand_cards.clear()
    dealer.choice = ""

    player1.hand_cards.append(deck1.draw_card())
    dealer.hand_cards.append(deck1.draw_card())


    print("\nPlayer Turn\n")
    print("Player1 has " + str(player1.show_hand()))
    player1_hand(player1, deck1)
    print("\nDealer Turn\n")
    print("Dealer has " + str(dealer.show_hand()))
    dealer_hand(dealer, deck1)
    result(dealer,player1)




if __name__ == "__main__":
    print("Welcome to BackJack Game")
    main()




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
