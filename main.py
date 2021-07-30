from random import choice
# Authors: Scott Woolfrey, Cody Coward, Nick Skinner

class Card:
    def __init__(self):
        self.type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # self.type = ["A", "A", "A", "A", "A", "A", "A", "A", "9", "10", "J", "Q", "K"]  # TESTING ACES **DELETE AFTER"
        self.cards = [[suite + num for num in self.type] for suite in ["♥", "♠", "♦", "♣"]]
        self.gameCards = self.cards.copy()

    def reset(self):
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
            print("\033[36mDEALER HAND\033[0;0m:", dealer.hand, sep="  ")
        else:
            print("\033[36mDEALER HAND\033[0;0m:", dealer.hand[0])
        print("\033[36mPLAYER HAND\033[0;0m:", *player.hand, sep="  ")
        print()

    def printWinningDetails(self, action, winner):
        self.printData()
        if any(action):
            print(action)
        else:
            print("\b")
        print(winner.win)
        print(f"Current Balance: \u001b[32m{player.bal}\033[0;0m")
        self.anotherRound()


    def compare(self, action, balance):
        dealer.reveal = True
        self.printData()
        pValue = player.handValue(player.hand)
        dValue = dealer.handValue(dealer.hand)
        print(pValue, dValue)

        # Black Jack
        if pValue == 21 and len(player.hand) == 2:
            player.bal = player.bal + player.bet * 3
            self.printWinningDetails("BLACK JACK", player)
        elif dValue == 21 and len(dealer.hand) == 2:
            player.bal -= player.bet
            self.printWinningDetails("BLACK JACK", dealer)

        # Bust
        if pValue > 21:
            self.printWinningDetails("", dealer)
        elif dValue > 21:
            player.bal += player.bet * 2
            self.printWinningDetails("", player)

        # Push
        if pValue == dValue:
            player.bal = player.bal + player.bet

        if action == "s":
            # Push
            if pValue == dValue:
                print("PUSH")
                print("======== NO WINNER ========")
                m.anotherRound()

            # Higher Hand Value
            if pValue > dValue:
                player.bal = player.bal + player.bet * 2
                self.printWinningDetails("", player)
            elif dValue > pValue:
                player.bal -= player.bet
                self.printWinningDetails("", dealer)
            self.anotherRound()
        self.loop()

    def anotherRound(self):
        play = input("Do you want to play again? [y/n]: ")
        if play == "y":
            player.bet = int(input("\nBetting Amount:\n"))
            card.reset()
            player.reset()
            dealer.reset()
            dealer.reveal = True
            m.loop()
        elif play == "n":
            exit()

    def loop(self):
        x = input("\nHIT: [1]  STAND: [2] --> ")
        if x == "1":    # Hit
            self.hit(player)
            self.compare(0, player.bal)
            self.loop()
        elif x == "2":  # Stand
            dealer.reveal = True
            dealer.dealerLogic()
            player.bal = self.compare("s", player.bal)


class User (Card):
    def __init__(self, name, bal, bet):
        super(Card).__init__()
        self.name = name
        self.bet = bet
        self.win = f"======== {self.name} WINS ========"
        self.hand = [card.draw(), card.draw()] # list of strings
        self.value = 0
        self.value = self.handValue(self.hand)  # int
        self.bal = bal
        print(f"Current Balance: \u001b[32m{self.bal}\033[0;0m")
        self.bal -= self.bet

    def handValue(self, hand):
        # Take the value of the 2nd character in the string.  1st character is the suite
        return sum([int(self.cardValue(i[1:])) for i in hand])

    def reset(self):
        self.hand.clear()
        self.hand = [card.draw(), card.draw()]
        self.value = 0



    def cardValue(self, card):
        # Convert face cards to 10
        if card == "A":
                card =  1 if self.value >= 11 else 11
        elif card == "K" or card == "Q" or card == "J":
            card = "10"
        return card


class Dealer (Card):
    def __init__(self, name):
        super(Card).__init__()
        self.name = name
        self.win = f"======== {self.name} WINS ========"
        self.hand = [card.draw(), card.draw()] # list of strings
        self.value = 0
        self.value = self.handValue(self.hand)  # int
        self.reveal = False

    def dealerLogic(self):
        if self.value < 17:
            while self.value < 17 and self.value < player.value:
                m.hit(dealer)
                self.value = self.handValue(self.hand)
        else:
            pass

    def reset(self):
        self.hand.clear()
        self.hand = [card.draw(), card.draw()]
        self.value = self.handValue(self.hand)
        self.reveal = False
        m.printData()

    def handValue(self, hand, ):
        # Take the value of the 2nd character in the string.  1st character is the suite
        return sum([int(self.cardValue(i[1:])) for i in hand])

    def cardValue(self, card):
        # Convert face cards to 10
        if card == "A":
                card =  1 if self.value >= 11 else 11
        elif card == "K" or card == "Q" or card == "J":
            card = "10"
        return card


card = Card()
bet = int(input("\nBetting Amount:\n"))
player = User("Player", 1000, bet)
dealer = Dealer("Dealer")
m = Main()
m.loop()

# COlOR OUTPUT
# print("\u001b[32mBLACK JACK\033[0;0m")
# print("\033[1;31mBUST\033[0;0m")
