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



class Player:
    def __init__(self):
        pass


card = Card("Card", 6)
card.show()