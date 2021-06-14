class Banker:
    def __init__(self):
        self.shelved=0
        self.balance=0
    
    def shelf(self,points):
        
        self.shelved=self.shelved+points
        
    def bank(self):
               
        self.balance=self.balance+self.shelved
        self.shelved=0
        

        return self.balance

    def clear_shelf(self):
     
        self.shelved=0
