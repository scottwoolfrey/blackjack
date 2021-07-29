from time import sleep
from random import choice


class Card:
    def __init__(self):
        self.type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [[suite + num for num in self.type] for suite in ["♥", "♠", "♦", "♣"]]
        self.gameCards = self.cards.copy()

    def draw(self):
        suite = choice(self.gameCards)
        num = choice(suite)
        suite.remove(num)
        # if the suite is empty, remove the suite from potential cards to pull
        if not suite:
            self.gameCards.remove(suite)
        return num

    def cardValue(self, card):
        # Convert monkey cards to 10
        if card == "A":
            print(player.value)
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


class Main:
    def __init__(self):
        self.printData()

    def hit(self, person):
        c = card.draw()
        (person.hand).append(card.cardValue(c))

    def printData(self):
        if dealer.reveal:
            print("DEALER HAND:", dealer.hand, sep="  ")
        else:
            print("DEALER HAND:", dealer.hand[0], sep="  ")
        print("PLAYER HAND:", *player.hand, sep="  ")
        print()

    def printWinningDetails(self, action, winner):
        if any(action):
            print(action)
        print(winner.win)
        exit()


    def compare(self, action):
        self.printData()
        pValue = card.handValue(player.hand)
        dValue = card.handValue(dealer.hand)

        # Black Jack
        if pValue == 21 and len(player.hand) == 2:
            self.printWinningDetails("BLACK JACK", player)
        elif dValue == 21 and len(dealer.hand) == 2:
            self.printWinningDetails("BLACK JACK", dealer)
        # Bust
        if pValue > 21:
            self.printWinningDetails("BUST", player)
        elif dValue > 21:
            self.printWinningDetails("BUST", dealer)
        # Max Hand Value
        elif pValue == 21:
            self.printWinningDetails("", player)
        elif dValue == 21:
            self.printWinningDetails("", dealer)

        if action == "s":
            # Push
            if pValue == dValue:
                self.printWinningDetails("PUSH", player)
            # Higher Hand Value
            if pValue > dValue:
                self.printWinningDetails("", player)
            elif dValue > pValue:
                self.printWinningDetails("", dealer)

        self.loop()

    def loop(self):
        x = input("\nHIT: [h]  STAND: [s]\n")
        if x == "h":
            self.hit(player)
            self.compare(x)
            self.loop()
        elif x == "s":
            dealer.reveal = True
            dealer.logic()
            self.compare(x)
            self.printData()


class User:
    def __init__(self, name):
        self.name = name
        self.win = "======== PLAYER WINS ========"
        self.hand = [card.draw(), card.draw()]  # list of strings
        self.value = card.handValue(self.hand)  # int
        self.balance = 1000

    def dealerlogic(self):
        if self.value < 17:
            while self.value < 17:
                # TO DO: if the dealer has an ace and counting it as 11 brings the total to 17 - 21, dealer must hit
                m.hit(dealer)
                self.value = card.handValue(self.hand)
        else:
            pass
class Dealer (Card):
    def __init__(self):
        super(Card).__init__()
        self.win = "======== DEALER WINS ========"
        self.hand = [card.draw(), card.draw()]
        self.value = card.handValue(self.hand)
        self.reveal = False

    def logic(self):
        if self.value < 17:
            while self.value < 17:
                # TO DO: if the dealer has an ace and counting it as 11 brings the total to 17 - 21, dealer must hit
                m.hit(dealer)
                self.value = card.handValue(self.hand)
        else:
            pass
card = Card()
print(card.cards)
player = User("Player")
# dealer = User("Dealer")
dealer = Dealer()
m = Main()

m.loop()

# COlOR OUTPUT
# print("\u001b[32mBLACK JACK\033[0;0m")
# print("\033[1;31mBUST\033[0;0m")
