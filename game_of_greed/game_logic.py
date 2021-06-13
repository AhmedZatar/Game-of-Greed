import random
from random import randint
from collections import Counter

scores={
   'straight':1500,
   'three pairs':750,


    (1, 1): 100,
    (1, 2): 200,
    (1, 3): 1000,
    (1, 4): 2000,
    (1, 5): 3000,
    (1, 6): 4000,
#___________________
    (2, 3): 200,
    (2, 4): 400,
    (2, 5): 600,
    (2, 6): 800,
#___________________    
    (3, 4): 600,
    (3, 5): 900,
    (3, 6): 1200,
#___________________  
    (4, 3): 400,
    (4, 4): 800,
    (4, 5): 1200,
    (4, 6): 1600,
#___________________   
    (5, 1): 50,
    (5, 2): 100,
    (5, 3): 500,
    (5, 4): 1000,
    (5, 5): 1500,
    (5, 6): 2000,
#___________________   
    (6, 3): 600,
    (6, 4): 1200,
    (6, 5): 1800,
    (6, 6): 2400,
}


class GameLogic:
    
    @staticmethod
    def roll_dice(num_dice):
          return tuple(random.randint(1,6) for _ in range(0,num_dice))

    def calculate_score(dice):
        score=0
        x=False
        
        dice=Counter(dice)
        print(dice.most_common())
        # [(3, 1), (1, 1), (6, 1), (2, 1), (5, 1), (4, 1)]
        print(len(dice.most_common()))

        if 1==1:
            pass
            # score=score+scores['straight']
        elif len(dice.most_common())==3 and dice.most_common(3)[2][1] == 2:
            score=score+scores['three pairs']
            print('hello')      
        else:
          for i in range(len(dice.most_common())):

              try:
                score=score+scores[(dice.most_common()[i][0]  ,dice.most_common()[i][1])]
              except KeyError:
                  score=score+0


        return score
            


if __name__=='__main__':
  print(GameLogic.calculate_score((2,2,3,3,4,4)))