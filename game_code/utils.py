import pygame
import os

def get_image(object, path):
    image = object._image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
        image = pygame.image.load(canonicalized_path)
        object._image_library[path] = image
    return image

def drawFrame(object, screen):
    path = object.path + object.state + "/" + (4-len(str(object.frame)))*'0' + str(object.frame) + '.png'
    screen.blit(get_image(object, path), (object.realX,object.realY))