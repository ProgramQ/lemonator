from random import randint
import sys, os
from world import World
from stand import Stand

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.BLUE = ''
        self.GREEN = ''
        self.WARNING = ''
        self.RED = ''
        self.ENDC = ''

def main():
    os.system('clear') 

    print colors.GREEN + "   __                         __          "
    print "  / /__ __ _  ___  ___  ___ _/ /____  ____  "
    print " / / -_)  ' \/ _ \/ _ \/ _ `/ __/ _ \/ __/ "
    print "/_/\__/_/_/_/\___/_//_/\_,_/\__/\___/_/   \n" + colors.ENDC

    username = raw_input("Choose a username: ")
    name = raw_input("What is the name of your lemonade stand: ")

    os.system('clear')

    world = World(15)
    user = Stand(25, 100, name, (randint(0,world.world_x - 2), 
        randint(0,world.world_y - 2)))

    world.stands.add(user)

    running = True
    while running:
        world.draw_map()
        print "Lemons: " + str(user.lemons) + "\tMoney: $" + str(user.balance)
        if user.has_ads_running() == True:
            print "You currently have [" + str(len(user.ads)) + "]"
        print
        choice = raw_input("[exit|buy|sell|new|ads]> ").lower()

        if choice.startswith("sell"):
            try:
                user.sell(int(choice[5:]))
            except:
                raw_input("Please provide a price for your lemonade")
        if choice.startswith("buy"):
            try:
                user.buy(int(choice[4:]))
            except:
                raw_input("Please provide an amount of lemons to buy")
        if choice == "ads":
            pass
        if choice == "new":
            world.stands.add(Stand(0, 100, name, 
                (randint(0,world.world_x - 2), randint(0,world.world_y -2))))
        if choice == "exit":
            exit(0)

        os.system('clear')

if __name__ == '__main__':
    main()
