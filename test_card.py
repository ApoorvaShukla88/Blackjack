import unittest
import card

from Blackjack.card import Card


class TestCard(unittest.TestCase):

    def test_value(self):
        card = Card(10, "J")
        card1 = Card(11, 'A')
        self.assertEqual(card.value(), 10)
        self.assertEqual(card1.value(), 11)


if __name__ == "__main__":
    unittest.main()
