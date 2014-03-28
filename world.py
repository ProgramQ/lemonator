import sys

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

class World:
    def __init__(self, max_stands):
        self.max_stands = max_stands
        self.stands = set()
        self.world_x = 25
        self.world_y = 15

    def draw_map(self):
        for y in range(self.world_y):
            for x in range(self.world_x):
                for stand in self.stands:
                    if stand.stand_coords == (x,y):
                        sys.stdout.write(colors.BLUE + '*' + colors.ENDC)
                    else:
                        sys.stdout.write('.')
            print
        print