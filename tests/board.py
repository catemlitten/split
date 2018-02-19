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

    def read_level(self, level_file):
        fileHand = open(level_file, 'r')
        y = 1
        x = 1
        for line in fileHand:
            for whatGoesThere in line:
                if(whatGoesThere == 'e'):
                    # nothing to make, but increment x
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
                # print(x,y)

    #Of course, this list won't be hard-coded, and will instead come from board.getTiles()
    '''
    tiles = [
        Tile(coin, 3, 3),
        Tile(thymbal, 4, 3),
        Tile(coin, 5, 3),
        Tile(coin, 6, 3),
        Tile(thymbal, 3, 4),
        Tile(coin, 4, 4),
        Tile(coin, 5, 4),
        Tile(coin, 6, 4),
        Tile(coin, 3, 5),
        Tile(coin, 4, 5),
        Tile(red_coin, 6, 5),
        Tile(coin, 3, 6),
        Tile(coin, 4, 6),
        Tile(coin, 7, 6),
        Tile(coin, 8, 6),
        Tile(coin, 9, 6),
        Tile(thymbal, 3, 7),
        Tile(coin, 4, 7),
        Tile(coin, 7, 7),
        Tile(coin, 8, 7),
        Tile(thymbal, 9, 7),
        Tile(coin, 3, 8),
        Tile(coin, 4, 8),
        Tile(coin, 5, 8),
        Tile(coin, 6, 8),
        Tile(coin, 7, 8),
        Tile(coin, 8, 8),
        Tile(thymbal, 10, 11),
        Tile(coin, 11, 11),
        Tile(coin, 12, 11),
        Tile(coin, 13, 11),
        Tile(coin, 14, 11),
        Tile(blue_coin, 5, 12),
        Tile(coin, 6, 12),
        Tile(thymbal, 7, 12),
        Tile(thymbal, 10, 12),
        Tile(coin, 11, 12),
        Tile(coin, 12, 12),
        Tile(coin, 13, 12),
        Tile(coin, 14, 12),
        Tile(coin, 6, 13),
        Tile(coin, 7, 13),
        Tile(coin, 8, 13),
        Tile(coin, 9, 13),
        Tile(coin, 10, 13),
        Tile(coin, 11, 13),
        Tile(coin, 12, 13),
        Tile(coin, 13, 13),
        Tile(coin, 14, 13)
        ]
    '''
    def getTiles(self, level_file):
        self.read_level(level_file)
        return self.tiles;

    def checkJump(playerOne, playerTwo):
        # if jump off cliff - die
        # else if jump onto new coin call update()
        # else if wall -- bounce
        return None
