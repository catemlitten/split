import pygame
import os
from board import *
from utils import *

class Player:

    _image_library = {}
    
    def __init__(self, path, x, y):
        self.path = path
        self.frame = 0
        self.x = x
        self.y = y
        self.d = 'idle'
        self.realX = (self.x - 1) * 50 - 12.5
        self.realY = (self.y - 1) * 35 + 8
        self.state = "idle"
        self.idleFrames = len(os.listdir(self.path + 'idle/'))
        self.jumpFrames = len(os.listdir(self.path + 'jump/'))

    def location(self, isReal):
        if isReal:
            if self.d == 'up':
                self.realY -= 35/self.jumpFrames
            elif self.d == 'down':
                self.realY += 35/self.jumpFrames
            elif self.d == 'left':
                self.realX -= 50/self.jumpFrames
            elif self.d == 'right':
                self.realX += 50/self.jumpFrames
        else:
            if self.d == 'up':
                self.y -= 1
            elif self.d == 'down':
                self.y += 1
            elif self.d == 'left':
                self.x -= 1
            elif self.d == 'right':
                self.x += 1

    def check_ahead(self, direction, board, screen):
        current_tile = board.board[self.y-1][self.x-1]
        if direction == 'up':
            try:
                next_tile = board.board[self.y - 2][self.x - 1]
                board.board[self.y-1][self.x-1] = 'e'
                if next_tile == 'w':
                    return ["wall", self.x, self.y]
                elif next_tile == 'e':
                    board.remove_tile(self.x, self.y, screen)
                    return ["dead", self.x, self.y-1]
                elif next_tile == 'q' or next_tile == 'p':
                    board.remove_tile(self.x, self.y, screen)
                    return ["victory", self.x, self.y-1]
                else:
                    board.remove_tile(self.x, self.y, screen)
                    return ["moving", self.x, self.y-1]
            except IndexError:
                    board.remove_tile(self.x, self.y, screen)
                    return ["dead", self.x, self.y-1]
        elif direction == 'down':
            try:                                                                       
                next_tile = board.board[self.y][self.x - 1]
                board.board[self.y-1][self.x-1] = 'e'
                if next_tile == 'w':
                    return ["wall", self.x, self.y]
                elif next_tile == 'e':
                    print("Ded.")
                    board.remove_tile(self.x-1, self.y, screen)
                    return ["dead", self.x, self.y+1]
                elif next_tile == 'q' or next_tile == 'p':
                    board.remove_tile(self.x-1, self.y, screen)
                    return ["victory", self.x-1, self.y+1]
                else:
                    board.remove_tile(self.x, self.y, screen)
                    return ["moving", self.x-1, self.y+1]
            except IndexError:
                    board.remove_tile(self.x, self.y, screen)
                    return ["dead", self.x-1, self.y+1]
        elif direction == 'right':
            try:
                next_tile = board.board[self.y - 1][self.x]
                board.board[self.y-1][self.x-1] = 'e'
                if next_tile == 'w':
                    return ["wall", self.x, self.y]
                elif next_tile == 'e':
                    board.remove_tile(self.x, self.y, screen)
                    return ["dead", self.x+1, self.y]
                elif next_tile == 'q' or next_tile == 'p':
                    board.remove_tile(self.x, self.y, screen)
                    return ["victory", self.x+1, self.y]
                else:
                    board.remove_tile(self.x, self.y, screen)
                    return ["moving", self.x+1, self.y]
            except IndexError:
                    board.remove_tile(self.x, self.y, screen)
                    return ["dead", self.x+1, self.y]
        elif direction == 'left':
            try:
                next_tile = board.board[self.y - 1][self.x - 2]
                board.board[self.y-1][self.x-1] = 'e'
                if next_tile == 'w':
                    return ["wall", self.x, self.y]
                elif next_tile == 'e':
                    board.remove_tile(self.x, self.y, screen)
                    return ["dead", self.x-1, self.y]
                elif next_tile == 'q' or next_tile == 'p':
                    board.remove_tile(self.x, self.y, screen)
                    return ["victory", self.x-1, self.y]
                else:
                    board.remove_tile(self.x, self.y, screen)
                    return ["moving", self.x-1, self.y]
            except IndexError:
                    board.remove_tile(self.x, self.y, screen)
                    return ["dead", self.x-1, self.y]

    def update(self, direction, screen, board):  # add board parameter to control jump
        self.frame += 1
        if self.state == "idle" and self.frame > self.idleFrames:
            self.frame = 1
        elif self.state == "jump" and self.frame > self.jumpFrames:
            self.frame = 1
            self.state = "idle"
            self.location(False)  # this is where the jump animation ends and the player position is updated.
            # we should have the board object update here (board.update(x, y, direction [d])), and check if the player just jumped off (died)
            self.d = "idle"
            self.frame = 1
        if self.state == "idle" and direction != "idle": # and board.check(x, y, direction [d]):
            self.d = direction
            # make a function to check the tile ahead based on the direction and only flip coin if not a wall
            whats_next = self.check_ahead(direction, board, screen)
            if whats_next[0] == "wall":
                print("Ouch") 
                return whats_next
            elif whats_next[0] == "dead":
                return whats_next
            else:
                self.state = "jump"
                self.frame = 1
                return whats_next
        if self.state == "jump":
            self.location(True)
        drawFrame(self, screen)
        return "alive"
