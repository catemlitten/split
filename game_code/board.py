from tile import *
from animator import *
import os
import pygame

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
        self.board = []
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/..'


    def read_level(self, level_file):
        fileHand = open(level_file, 'r')
        y = 1
        x = 1
        for line in fileHand:
            boardLine = []
            line = line.rstrip()
            for whatGoesThere in line:
                if whatGoesThere != '\n':
                    boardLine.append(whatGoesThere)
                if whatGoesThere == 'e':
                    # nothing to make, but increment x
                    self.emptySpots.append([x, y])
                    x += 1
                elif whatGoesThere == 't':
                    self.tiles.append(Tile(self.coin, x, y))
                    x += 1
                elif whatGoesThere == 'w':
                    self.tiles.append(Tile(self.thymbal, x, y))
                    x += 1
                elif whatGoesThere == 'q':
                    self.tiles.append(Tile(self.red_coin, x, y))
                    x += 1
                elif whatGoesThere == 'p':
                    self.tiles.append(Tile(self.blue_coin, x, y))
                    x += 1
                elif whatGoesThere == '1':
                    self.player1[0] = x
                    self.player1[1] = y
                    self.tiles.append(Tile(self.coin, x, y))
                    x += 1
                elif whatGoesThere == '2':
                    self.player2[0] = x
                    self.player2[1] = y
                    self.tiles.append(Tile(self.coin, x, y))
                    x += 1
                else:
                    print("Something went wrong.")
            y += 1  # increment y access
            x = 1  # reset x
            self.board.append(boardLine)

    def get_tiles(self, level_file):
        self.read_level(level_file)
        return self.tiles;

    def remove_tile(self, x, y, screen):
        for tile in self.tiles:
            if tile.x == x and tile.y == y:
                self.tiles.remove(tile)
