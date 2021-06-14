class Game:
    def __init__(self,roller=None):
        self.roller=roller

 
    def  play(self):
        print('Welcome to Game of Greed')
        user_input=input('wanna play?') 
        if user_input=='n':
            print('OK. Maybe another time')  
        elif user_input=='y':
            score=0
            banking=0
            roundes=6
            round=1
            print(f'Starting round {1}') 
            print(f'Rolling {roundes} dice...')
            dice=self.roller(6)
            printable_dice = ','.join([str(d) for d in dice])
            print(printable_dice)
            user_choice=input('Enter dice to keep (no spaces), or (q)uit: q')
            if user_choice=='q':
                print('Thanks for playing. You earned 0 points')
#4,4,5,2,3,1
            else:
                if user_choice==str(5):
                    banking=50
                elif user_choice==str(1):
                    banking=100   
                print(f'You have {banking} unbanked points and 5 dice remaining')     

