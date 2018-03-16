import pygame
import os
from board import *
from utils import *

class DeadPlayer:

    _image_library = {}
    
    def __init__(self, path, x, y):
        self.path = path
        self.frame = 0
        self.x = x
        self.y = y
        self.d = 'death'
        self.realX = (self.x - 1) * 50 - 12.5
        self.realY = (self.y - 1) * 35 + 8
        self.state = "death"
        self.idleFrames = len(os.listdir(self.path + 'death/'))

    def update(self, direction, screen, board):
        self.frame += 1
        if self.state == "death" and self.frame > self.idleFrames:
            self.frame = 1
        drawFrame(self, screen)
        return "alive"
