# deck of cards exercise

class Card:
    def __init__(self, suit, card):
        self.suit = suit
        self.card = card

    def __repr__(self):
        return f'{self.card!r} of {self.suit!r}'


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        cards = ['A', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, card) for suit in suits for card in cards]

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min(count, num)

        if count == 0:
            raise ValueError('All cards have been dealt')

        # get the last 'actual' number of cards from the deck:
        # - we use negative indexing to get the last 'actual' number of cards from the deck,
        # - and then we update the deck to remove those cards.
        # - for example, if we have a deck of 52 cards and we want to deal 5 cards, we will get the last 5 cards from the deck (cards[-5:]),
        # - and then we will update the deck to remove those cards (cards[:-5]).
        # - if we want to deal more cards than are left in the deck, we will just get all the remaining cards from the deck (cards[-count:]),
        # - and then we will update the deck to remove those cards (cards[:-count]).
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        import random
        random.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)


c = Card('Hearts', '2')
print(c)  # Output: '2 of Hearts'

d = Deck()
print(d)  # Output: Deck of 52 cards
print(d.count())  # Output: 52
d.shuffle()
hand = d.deal_hand(5)
# Output: [Card('Hearts', '2'), Card('Diamonds', '5'), Card('Clubs', 'A'), Card('Spades', '10'), Card('Hearts', 'Jack')]
print(hand)
print(d.count())  # Output: 47
