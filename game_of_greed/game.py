from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self,roller=None):
        self.roller=roller

    def newRound(self,banker,round,total,dice_reminde):
        
        print(f'Starting round {round}')
        print(f'Rolling {dice_reminde} dice...')
        dice=self.roller(dice_reminde)
        printable_dice = ','.join([str(d) for d in dice])
        print(printable_dice)
        user_choice=input('Enter dice to keep (no spaces), or (q)uit: ')
        if user_choice=='q':
            if round>1:
                print(f'Total score is {banker.balance} points')

            print(f'Thanks for playing. You earned {banker.balance} points')
        else:
            user_choice_list=[]
            
            for i in range(len(user_choice)):
                    
                user_choice_list.append(int(user_choice[i]))
                
            score = GameLogic.calculate_score(tuple(user_choice_list))
            banker.shelf(score)
            total = banker.shelved
            dice_reminde=dice_reminde-len(user_choice_list)

            print(f'You have {total} unbanked points and {dice_reminde} dice remaining')
            
            user_choice=input('(r)oll again, (b)ank your points or (q)uit ')
            if user_choice=='b':
                banker.bank()
                print(f'You banked {total} points in round {round}')
                round+=1
                print(f'Total score is {banker.balance} points')
                banker.clear_shelf() 
                dice_reminde=6
                self.newRound(banker,round,total,dice_reminde)
                
            elif user_choice=='r':
                round+=1
                self.newRound(banker,round,total,dice_reminde)
            
            elif user_choice=='q':
                banker.bank()

                print(f'Thanks for playing. You earned {banker.balance} points')


    def  play(self):

        banker=Banker()   
        print('Welcome to Game of Greed')
        user_input=input('Wanna play? ') 
        if user_input=='n':
            print('OK. Maybe another time')
        elif user_input=='y':
            banking=0
            round=1
            dice_reminde=6
            self.newRound(banker,round,banking,dice_reminde)
             
            
            
            
                    


if __name__ == "__main__":
    roller = GameLogic.roll_dice
    game = Game(roller)
    game.play()
