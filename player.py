import random


class Player():

    def __init__(self):
        self.hand_cards = []
        self.choice = ""

    def no_of_cards_in_hand(self):
        while len(self.hand_cards) != 2:
            self.hand_cards.append(random.randint(1, 11))
        if len(self.hand_cards) == 2:
            print("You Have " + self.hand_cards)

            no_of_cards = len(self.hand_cards)

        for i in range(no_of_cards):
            card = self.hand_cards[i]

    def total_points(self):
        rank = 0
        for i in self.hand_cards:
            rank += card.rank

        if rank > 21:
            for card in self.hand_cards:
                if rank == 11:
                    rank -= 10
        else:
            return rank



    def welcome(self):
        print("Welcome to BackJack Game")








