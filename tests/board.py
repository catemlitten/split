from tile import *

class Board:

    def __init__(self):
        self.coin = '/animation/coin.png'
        self.thymbal = '/animation/thymbal.png'
        self.red_coin = '/animation/coin_red.png'
        self.blue_coin = '/animation/coin_blue.png'
        self.tiles = []
        self.player1 = [0, 0]
        self.player2 = [0, 0]
        self.emptySpots = []

    def read_level(self, level_file):
        fileHand = open(level_file, 'r')
        y = 1
        x = 1
        for line in fileHand:
            for whatGoesThere in line:
                if(whatGoesThere == 'e'):
                    # nothing to make, but increment x
                    self.emptySpots.append([x, y])
                    x += 1
                elif(whatGoesThere == 't'):
                    self.tiles.append(Tile(self.coin, x, y))
                    x += 1
                elif(whatGoesThere == 'w'):
                    self.tiles.append(Tile(self.thymbal, x, y))
                    x += 1
                elif(whatGoesThere == 'q'):
                    self.tiles.append(Tile(self.red_coin, x, y))
                    x += 1
                elif(whatGoesThere == 'p'):
                    self.tiles.append(Tile(self.blue_coin, x, y))
                    x += 1
                elif(whatGoesThere == '1'):
                    self.player1[0] = x
                    self.player1[1] = y
                    print(self.player1)
                    self.tiles.append(Tile(self.coin, x, y))
                    x += 1
                elif(whatGoesThere == '2'):
                    self.player2[0] = x
                    self.player2[1] = y
                    self.tiles.append(Tile(self.coin, x, y))
                    x += 1
                else:
                    print("Blank space? Why? strip() does not work")
            y += 1 # increment y access
            x = 1 # reset x

    def getTiles(self, level_file):
        self.read_level(level_file)
        return self.tiles;

    def checkJump(self, playerOne, playerTwo):
        # if jump off cliff - die
        # else if jump onto new coin call update()
        # else if wall -- bounce
        return None
