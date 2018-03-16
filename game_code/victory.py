import pygame
import os
from board import *
from utils import *

class Victor:

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

    def update(self, direction, screen, board):  # add board parameter to control jump
        self.frame += 1
        if self.state == "idle" and self.frame > self.idleFrames:
            self.frame = 1
        drawFrame(self, screen)
        return "alive"
