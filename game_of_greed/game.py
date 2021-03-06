from game_of_greed import game_logic
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self,roller=None):
        self.roller=roller or GameLogic.roll_dice
        self.quitnumber=1

    def newRound(self,banker,round,total,dice_reminde):
        
    
        print(f'Starting round {round}')
        self.roundstart(banker,round,total,dice_reminde)
               
                   
    def bank(self,banker,round,total,dice_reminde):
        banker.bank()
        print(f'You banked {total} points in round {round}')
        round+=1
        print(f'Total score is {banker.balance} points')
        dice_reminde=6
        self.newRound(banker,round,total,dice_reminde)


    def quit(self,banker):
              
        print(f'Total score is {banker.balance} points')

        print(f'Thanks for playing. You earned {banker.balance} points')
        self.quitnumber=0
    

    
    def startplay(self,banker,round,total,dice_reminde,printable_dice,dice):




        
        print(printable_dice)
        x= self.zlich(dice)
        if not x:
            print('Zilch!!! Round over')
            print(f'You banked 0 points in round {round}')
            print(f'Total score is {banker.balance} points')
            banker.clear_shelf()
            round+=1
            dice_reminde=6

            self.newRound(banker,round,total,dice_reminde)
        
        if(self.quitnumber):
          user_choice=input('Enter dice to keep (no spaces), or (q)uit: ')
        else:
            return
                
        if user_choice=='q':

            self.quit(banker)
            
        else:
            user_choice_list=[]
            
            for i in range(len(user_choice)):
                    
                user_choice_list.append(int(user_choice[i]))


            x=self.cheat(dice,user_choice_list)
            
            if not x:
              self.startplay(banker,round,total,dice_reminde,printable_dice,dice)
            else:

               self.rbq(banker,round,dice_reminde,user_choice_list)
            
    def cheat(self,dice,userselect):
      dice = list(dice)

      if len(userselect)>len(dice):
        print ('Cheater!!! Or possibly made a typo...')
        return False
      for i in userselect:
        if i in dice:
          dice.remove(i)
        else:
          print ('Cheater!!! Or possibly made a typo...')
          return False  
      return True

    def zlich(self,dice):
        score = GameLogic.calculate_score(dice)
        if score==0:
            return False
        else:
            return True


    def rbq(self,banker,round,dice_reminde,user_choice_list):
            score = GameLogic.calculate_score(tuple(user_choice_list))
            banker.shelf(score)
            total = banker.shelved
            dice_reminde=dice_reminde-len(user_choice_list)

            print(f'You have {total} unbanked points and {dice_reminde} dice remaining')

            if dice_reminde==0 and (total == 750 or total==1500 or total==4000 or total==800 or total==1200 or total==1600 or total==2000 or total==2400):
                dice_reminde=6
            
            user_choice=input('(r)oll again, (b)ank your points or (q)uit ')
            if user_choice=='b':
                self.bank(banker,round,total,dice_reminde)
                              
            elif user_choice=='r':
            
                self.roundstart(banker,round,total,dice_reminde)
            
            elif user_choice=='q':
                self.quit(banker)
                return
    
    def roundstart(self,banker,round,total,dice_reminde):

        if round > 20:
            self.quit(banker)
        else:

            if dice_reminde == 0:
                dice_reminde=6
             
            print(f'Rolling {dice_reminde} dice...')
            dice=self.roller(dice_reminde)

            printable_dice = ','.join([str(d) for d in dice])
            self.startplay(banker,round,total,dice_reminde,printable_dice,dice)



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
    game = Game()
    game.play()
