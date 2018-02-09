import pygame
import os

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
        self.idleFrames = 30
        self.jumpFrames = 27

    def get_image(self, path):
        image = self._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            self._image_library[path] = image
        return image

    def drawFrame(self, sc):
        sc.blit(self.get_image(self.path + self.state + "\\" + (4-len(str(self.frame)))*'0' + str(self.frame) + '.png'), (self.realX,self.realY))

    def location(self, isReal):
        if isReal:
            if self.d == 'up':
                self.realY -= 35/27
            elif self.d == 'down':
                self.realY += 35/27
            elif self.d == 'left':
                self.realX -= 50/27
            elif self.d == 'right':
                self.realX += 50/27
        else:
            if self.d == 'up':
                self.y -= 1
            elif self.d == 'down':
                self.y += 1
            elif self.d == 'left':
                self.x -= 1
            elif self.d == 'right':
                self.x += 1

    def update(self, d, sc):
        self.frame += 1
        if self.state == "idle" and self.frame > self.idleFrames:
            self.frame = 1
        elif self.state == "jump" and self.frame > self.jumpFrames:
            self.frame = 1
            self.state = "idle"
            self.location(False)
            self.d = "idle"
            self.frame = 1
        if self.state == "idle" and d != "idle":
            self.d = d
            self.state = "jump"
            self.frame = 1
        if self.state == "jump":
            self.location(True)
        self.drawFrame(sc)