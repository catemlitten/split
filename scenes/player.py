import pygame
import os
from board import *

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

    def get_image(self, path):
        image = self._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
            image = pygame.image.load(canonicalized_path)
            self._image_library[path] = image
        return image

    def drawFrame(self, sc):
        sc.blit(self.get_image(self.path + self.state + "/" + (4-len(str(self.frame)))*'0' + str(self.frame) + '.png'), (self.realX,self.realY))

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
        if direction == 'up':
            next_tile = board.board[self.y - 2][self.x - 1]
            if next_tile == 'w':
                return "wall"
            elif next_tile == 'e':
                print("Ded.")
                board.remove_tile(self.x, self.y, screen)
                return "dead"
            else:
                board.remove_tile(self.x, self.y, screen)
                return True
        elif direction == 'down':
            next_tile = board.board[self.y][self.x - 1]
            if next_tile == 'w':
                return "wall"
            elif next_tile == 'e':
                print("Ded.")
                board.remove_tile(self.x, self.y, screen)
                return "dead"
            else:
                board.remove_tile(self.x, self.y, screen)
                return True
        elif direction == 'right':
            next_tile = board.board[self.y - 1][self.x]
            if next_tile == 'w':
                return "wall"
            elif next_tile == 'e':
                print("Ded.")
                board.remove_tile(self.x, self.y, screen)
                return "dead"
            else:
                board.remove_tile(self.x, self.y, screen)
                return True
        elif direction == 'left':
            next_tile = board.board[self.y - 1][self.x - 2]
            if next_tile == 'w':
                return "wall"
            elif next_tile == 'e':
                print("Ded.")
                board.remove_tile(self.x, self.y, screen)
                return "dead"
            else:
                board.remove_tile(self.x, self.y, screen)
                return True

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
            if whats_next == "wall":
                print("Ouch") # we should have a self.state = "wall"
            elif whats_next == "dead":
                return "dead"
            else:
                # board.remove_tile(self.x, self.y)
                self.state = "jump"
                self.frame = 1
        if self.state == "jump":
            self.location(True)
        self.drawFrame(screen)
        return "alive"
