import random


class Card:
    def __init__(self):
        self.type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = [[suite + num for num in self.type] for suite in ["♥", "♠", "♦", "♣"]]
        self.gameCards = self.cards.copy()
        self.v = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def draw(self):
        suite = random.choice(self.gameCards)
        num = random.choice(suite)
        # # Print hearts and diamonds red in the terminal
        # if num[0] == "♦" or num[0] == "♥":
        #     print(f"\033[1;31m{num[0]}\033[0;0m{num[1]}")
        # else:
        #     print(num)
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
        return sum([int(self.cardValue(i[1:])) for i in hand])

card = Card()


class Main:
    def __init__(self):
        self.bust = False
        self.v = card.handValue(player.hand)

    def hit(self):
        c = card.draw()
        (player.hand).append(card.cardValue(c))

    def event(self):
        v = card.handValue(player.hand)
        if v == 21:
            print(card.handValue(player.hand), player.hand)
            print("\u001b[32mBLACK JACK\033[0;0m")
        elif v > 21:
            print(card.handValue(player.hand), player.hand)
            print("\033[1;31mBUST\033[0;0m")
        else:
            self.loop()

    def gameRound(self):
        pass


    def loop(self):
        print(card.handValue(player.hand), player.hand)
        x = input("\n"
                  "HIT: [h]  STAND: [s]\n")
        if x == "h":
            self.hit()
        elif x == "s":
            pass
        self.event()

class User:
    def __init__(self, name):
        self.name = name
        self.hand = [card.draw(), card.draw()]
        self.value = card.handValue(self.hand)

    def main(self):
        print()

    # if the player decides to hit and their score is 10 or under:
    #       set the value of the ace to 11

player = User("Player")
m = Main()
# player = User("Player")
m.loop()


class Dealer(Main):
    def __init__(self):
        self.hand = 0

    def draw(self):
        ace = random.choice([1,11])
        values = [ace,ace,ace,ace,2,3,4,5,6,7,8,9,10,10,10,10]
        y = random.choice(values)
        print(y)
        return y

    def logic(self):
        card = self.draw()
        # stand if total is 17 or more
        # if total under 16, keep hitting until 17 or more
        # if the dealer has an ace and counting it as 11 brings the total from 17 to 21, dealer must hit
        pass

d = Dealer()
d.draw()
