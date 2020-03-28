import unittest
import card

from Blackjack.card import Card


class TestCard(unittest.TestCase):


    def test_card(self):
        test_cases = [
            ('J', 10),
            ('A', 11),
            ('A', 1),
            ('2', 2),
            ('6', 6),
            ('K', 10)
        ]

        for actual, expected in test_cases:
            with self.subTest(f"{actual} -> {expected}"):
                card = Card()
                self.assertEqual(expected, card.value(actual))


if __name__ == '__main__':
    unittest.main()
