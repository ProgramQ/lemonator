from random import randint 

class Stand: 
    def __init__(self,balance,lemons,name,coords):
        self.balance = balance
        self.lemons = lemons
        self.name = name
        self.stand_coords = coords
        self.ads = set()
        
    def sell(self, cost):
        if self.lemons == 0:
            raw_input("You need to order more lemons!")
            return

        sold = 0

        for n in range(100):
            if randint(0, cost) == 1:
                self.balance += cost
                self.lemons -= 1
                sold += 1

                if self.lemons <= 0:
                    if self.balance < 3:
                        print "You have no more money - Game Over!"
                        sys.exit()
                    else:
                        print "You ran out of lemons."
                        break
        raw_input("Sold " + str(sold) + " glasses of lemonade")
            
    def buy(self, amount):
        oldBalance = self.balance
        oldLemons = self.lemons
        discount = 0
        if amount >= 100:
            discount += (amount / 100)
        try:
            choiceN = amount
            self.lemons += choiceN
            self.balance -= (2 * choiceN) - (discount * 50)
            if self.balance < 0:
                self.lemons = oldLemons
                self.balance = oldBalance
                raw_input("You can't buy that many, you don't have enough money.")
        except:
            print "You can't do that?"

    def has_ads_running(self):
        if len(self.ads) > 0:
            return True
        else:
            return False