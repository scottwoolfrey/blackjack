import random
import numpy as np


class Card:
    def __init__(self):
        self.type = ["A", "2", "3","4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        self.cards = [[suite + num for num in self.type] for suite in ["H","S","D","C"]]
        self.gameCards = self.cards.copy()
        self.value = [0,2,3,4,5,6,7,8,9,10,10,10,10]
        
    def draw(self):
        suite = random.choice(self.gameCards)
        num = random.choice(suite)
        print(num)
        suite.remove(num)
        
        # if the suite is empty, remove the suite from potential cards to pull
        if not suite:
            self.gameCards.remove(suite)
        return num
    
    def value(self):
        pass


card = Card()


class User (Card):
    def __init__(self, name):
        super(Card).__init__()
        self.name = name
        self.score = 0
        
    def user_score(self):
        temp = re.findall(r'\d+', self.draw())
        print(temp)
        self.score += temp
        print(self.score)
    # draw a card
    
    # convert non-numerical cards to numerical values (A, K, Q, J -> x, 10, 10, 10)
    def main(self):
        self.cards.index(self.score)
        print()
    # if the player decides to hit and their score is 10 or under:
    #       set the value of the ace to 11
    
    
# for i in range(int(input("How many players?"))):
#     Player = User(f"Player{i}")
player = User("Player")

class Dealer (Card):
    def __init__(self):
        self.hand = 0
        
    
    def logic(self):
        card = self.draw()
        
        # stand if total is 17 or more
        # if total under 16, keep hitting until 17 or more
        # if the dealer has an ace and counting it as 11 brings the total from 17 to 21, dealer must hit
        
        pass

d = Dealer()


class Main:
    def __init__(self):
        self.bust = False
    
    def hit(self):
        pass
    
    def stand(self):
        pass
    
    def bust(self):
        pass
    
    def gameRound(self):
        pass
    
    def blackJack(self):
        # player's card value is 21, which pays out 3:2
        pass
    
    def dealerRules(self):
        pass
