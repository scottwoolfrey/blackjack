import random
import numpy as np

print(np.arange(9))
class Suites:
    def __init__(self):
        self.type = ["A", "2", "3","4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        self.cards = [[suite + num for num in self.type] for suite in ["H","S","D","C"]]
        self.gameCards = self.cards.copy()
        self.value = [0,2,3,4,5,6,7,8,9,10,10,10,10]
        
    def draw(self):
        for i in range(52):
            suite = random.choice(self.cards)
            num = random.choice(suite)
            print(num)
            suite.remove(num)
            print("elements in list:", len(suite))
            
            # if the suite list is empty
            if not suite:
                self.cards.remove(suite)

s = Suites()
s.draw()

class Player:
    def __init__(self):
        pass
    
    def score(self):
        pass
#tot_score = 