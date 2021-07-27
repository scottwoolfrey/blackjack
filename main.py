from random import randint


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for n in range(1, 14):
                self.cards.append(Card(s, n))

    def show(self):
        for cd in self.cards:
            cd.show()


    def shuffle_deck(self):
        for sd in range(len(self.cards) -1, 0, -1):




class Player:
    def __init__(self):
        pass


deck = Deck()
deck.show()