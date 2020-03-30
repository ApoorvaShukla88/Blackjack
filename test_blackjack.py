import unittest
import sys

import card

from Blackjack.card import Card
from Blackjack.player import Player


class TestBlackjack(unittest.TestCase):

    def test_player1_hand(self):
        p1 = Player()
        self.assertEqual(p1.total_points() > 21, p1.total_points().sys.stdout)
        self.assertEqual(p1.total_points() == 21, True)







if __name__ == "__main__":
    unittest.main()
