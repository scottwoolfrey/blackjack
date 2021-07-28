import random


class Card:
    def __init__(self):
        self.type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [[suite + num for num in self.type] for suite in ["♥", "♠", "♦", "♣"]]
        self.gameCards = self.cards.copy()

    def draw(self):
        suite = random.choice(self.gameCards)
        num = random.choice(suite)
        suite.remove(num)
        # if the suite is empty, remove the suite from potential cards to pull
        if not suite:
            self.gameCards.remove(suite)
        return num

    def cardValue(self, card):
        # Convert monkey cards to 10
        if card == "K" or card == "Q" or card == "J" or card == "A":
            # Automatically turn a soft ace into a hard ace
            # if card == "A" and currentHandValue[0] < 10:
            #     card = "11"
            # else:
            #     card = "1"
            card = "10"
        return card

    def handValue(self, hand):
        # Take the value of the 2nd character in the string.  1st character is the suite
        return sum([int(self.cardValue(i[1:])) for i in hand])

card = Card()


class Main:
    def __init__(self):
        self.bust = False
        self.printData()

    def hit(self, person):
        c = card.draw()
        (person.hand).append(card.cardValue(c))

    def stand(self):
        pass

    def printData(self):
        if dealer.reveal:
            print("DEALER HAND:", dealer.hand)
        else:
            print("DEALER HAND:", dealer.hand[0])
        print("PLAYER HAND:",player.hand)

    def compare(self):
        self.printData()
        v1 = player.value
        v2 = dealer.value

        # Push
        if v1 == v2:
            print("PUSH")

        # Winner
        if v1 == 21 or v1 < v2:
            print("PLAYER WINS")
        elif v2 == 21 or v2 < v1:
            print("DEALER WINS")

    def event(self, pValue, dValue):
        v1 = dealer.value
        v2  = player.value

        if v1 == 21:
            print(card.handValue(player.hand), player.hand)
            print("\u001b[32mBLACK JACK\033[0;0m")

        elif v1 or v2 > 21:
            print(dealer.hand)
            print(card.handValue(player.hand), player.hand)
            print("\033[1;31mBUST\033[0;0m")
        else:
            self.printData()
            self.loop()

    def loop(self):
        print("PLAYER:\n", player.hand)

        x = input("\nHIT: [h]  STAND: [s]\n")
        if x == "h":
            self.hit(player)
        elif x == "s":
            dealer.logic()
            dealer.reveal = True
        self.compare()


class User:
    def __init__(self, name):
        self.name = name
        self.hand = [card.draw(), card.draw()]  # list of strings
        self.value = card.handValue(self.hand)  # int


class Dealer (Card):
    def __init__(self):
        super(Card).__init__()
        self.hand = [card.draw(), card.draw()]
        self.value = card.handValue(self.hand)
        self.reveal = False

    def logic(self):
        card.cardValue(card.draw())

        if self.value >= 17:
            pass
        else:
            while self.value < 17:
                # TO DO: if the dealer has an ace and counting it as 11 brings the total to 17 - 21, dealer must hit
                m.hit(dealer)
                self.value = card.handValue(self.hand)

player = User("Player")
dealer = Dealer()

m = Main()
m.loop()


