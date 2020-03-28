import random
import os

player_cards = []

while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You Have "+ player_cards)