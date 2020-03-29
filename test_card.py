import unittest
import card

from Blackjack.card import Card


class TestCard(unittest.TestCase):

    def test_value(self):
        card = Card(10, "J")
        card1 = Card(11, 'A')
        card2 = Card(1, 'A')
        self.assertEqual(card.value(), 10)
        self.assertEqual(card1.value(), 11)
        self.assertEqual(card2.value(), 1)

if __name__ == "__main__":
    unittest.main()
