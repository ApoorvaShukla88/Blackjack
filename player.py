import random
import os

player_cards = []

while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You Have "+ player_cards)


while sum(player_cards) < 21:
    player_action = str(input("Do you want HIT or STAY "))
    if player_action == 'HIT':
        player_cards.append((random.randint(1,11)))
        print("Now Player has "+ str(sum(player_cards) + "with these cards" + player_cards))
    else:
        print("You have "+ str(sum(player_cards) + "with these cards" + player_cards))
