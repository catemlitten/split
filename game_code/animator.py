import pygame
import os

class Animator:
    
    _image_library = {}
    
    def __init__(self, path, x, y):
        self.path = path
        self.frame = 0
        self.x = x
        self.y = y
        self.realX = (self.x - 1) * 50 - 12.5
        self.realY = (self.y - 1) * 35 + 20
        self.nFrames = len(os.listdir(self.path))

    def get_image(self, path):
        image = self._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
            image = pygame.image.load(canonicalized_path)
            self._image_library[path] = image
        return image

    def drawFrame(self, sc):
        sc.blit(self.get_image(self.path + (4-len(str(self.frame)))*'0' + str(self.frame) + '.png'), (self.realX,self.realY))

    def update(self, sc):
        self.frame += 1
        if self.frame > self.nFrames:
            self.frame = 1
        self.drawFrame(sc)