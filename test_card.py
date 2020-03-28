import unittest
import card

from Blackjack.card import Card


class TestCard(unittest.TestCase):

    def test_value(self):
        self.assertEqual(Card.value('J'), 10)
        self.assertEqual(Card.value('A'), 11)


if __name__ == "__main__":
    unittest.main()
