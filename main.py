from time import sleep
from random import choice


class Card:
    def __init__(self):
        self.type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # self.type = ["A", "A", "A", "A", "A", "A", "A", "A", "9", "10", "J", "Q", "K"]  # TESTING ACES **DELETE AFTER"
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


class Main:
    def __init__(self):
        self.printData()

    def hit(self, person):
        c = card.draw()
        (person.hand).append(person.cardValue(c))

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
        pValue = player.handValue(player.hand)
        dValue = dealer.handValue(dealer.hand)

        # Black Jack
        if pValue == 21 and len(player.hand) == 2:
            self.printWinningDetails("BLACK JACK", player)
        else:
            self.printWinningDetails("BLACK JACK", dealer)

        # Bust
        if pValue > 21:
            self.printWinningDetails("BUST", dealer)
        elif dValue > 21:
            self.printWinningDetails("BUST", player)

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
            dealer.dealerlogic()
            self.compare(x)
            self.printData()


class User (Card):
    def __init__(self, name):
        super(Card).__init__()
        self.name = name
        self.win = f"======== {self.name} WINS ========"
        self.hand = [card.draw(), card.draw()] # list of strings
        self.value = 0
        self.value = self.handValue(self.hand)  # int
        self.balance = 1000
        self.reveal = False

    def dealerlogic(self):
        if self.value < 17:
            while self.value < 17:
                # TO DO: if the dealer has an ace and counting it as 11 brings the total to 17 - 21, dealer must hit
                m.hit(dealer)
                self.value = self.handValue(self.hand)
        else:
            pass

    def handValue(self, hand):
        # Take the value of the 2nd character in the string.  1st character is the suite
        return sum([int(self.cardValue(i[1:])) for i in hand])

    def cardValue(self, card):
        # Convert face cards to 10
        if card == "A":
            if self.value >= 11:
                card = "1"
            else:
                card = "11"
            print(self.value)

        if card == "K" or card == "Q" or card == "J":
            card = "10"
        return card

card = Card()
player = User("Player")
dealer = User("Dealer")
m = Main()
m.loop()

# COlOR OUTPUT
# print("\u001b[32mBLACK JACK\033[0;0m")
# print("\033[1;31mBUST\033[0;0m")
