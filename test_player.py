import unittest
import card

from Blackjack.card import Card
from Blackjack.player import Player


class TestCard(unittest.TestCase):

    def test_total_points(self):
        p1 = Player()
        self.assertEqual(p1.total_points(), sum(p1.hand_cards))





if __name__ == "__main__":
    unittest.main()
