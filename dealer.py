from random import random

dealer_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has X and " + dealer_cards[1])

