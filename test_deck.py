import unittest
from Blackjack.card import Card

from Blackjack import deck
from Blackjack.deck import Deck


class TestDeck(unittest.TestCase):

    def test_draw_card(self):
        deck = Deck()
        deck.reset()
        self.assertIsInstance(deck.draw_card(), Card)

    def test_deck_count(self):
        deck2 = Deck()
        deck2.reset()
        self.assertEqual(len(deck2.cards), 52)
