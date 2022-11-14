import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:


    def __init__(self):
        self.ranks = [str(n) for n in range(1,11)] + list('JQKA')
        self.suits = 'spades diamonds clubs hearts'.split()
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

print(len(deck))
print(deck[10])
print(choice(deck))
