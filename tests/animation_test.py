from player import *
from animator import *
import pygame
import os

_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    clock = pygame.time.Clock()
    path = os.path.dirname(os.path.realpath(__file__)) + '\\..'

    direction = '-'

    p1 = Player(path + '\\animation\\character1\\', 9, 6)
    p2 = Player(path + '\\animation\\character2\\', 12, 11)
    anims = [	
    	Animator(path + '\\animation\\coin\\', 9, 3),
    	Animator(path + '\\animation\\dice2\\', 3, 12),
    	Animator(path + '\\animation\\dice1\\', 14, 4),
    	Animator(path + '\\animation\\pin2\\', 12, 9)
    ]
    tiles = [
    	[3,3],[5,3],[6,3],
    	[4,4],[5,4],[6,4],
    	[3,5],[4,5],
    	[3,6],[4,6],[7,6],[8,6],[9,6],
    	[4,7],[7,7],[8,7],
    	[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],
    	[11,11],[12,11],[13,11],[14,11],
    	[6,12],[11,12],[12,12],[13,12],[14,12],
    	[6,13],[7,13],[8,13],[9,13],[10,13],[11,13],[12,13],[13,13],[14,13]
    ]
    walls = [
    	[4,3],
    	[3,4],
    	[3,7],[9,7],
    	[10,11],
    	[7,12],[10,12]
    ]
    tileRed = [6,5]
    tileBlue = [5,12]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if pygame.key.get_pressed()[pygame.K_w]:
            direction = 'up'
        elif pygame.key.get_pressed()[pygame.K_a]:
            direction = 'left'
        elif pygame.key.get_pressed()[pygame.K_s]:
            direction = 'down'
        elif pygame.key.get_pressed()[pygame.K_d]:
            direction = 'right'
        else:
        	direction = 'idle'

        screen.fill((255, 255, 255))
        screen.blit(get_image(path + '\\animation\\bg_2.png'), (0, 0))
        screen.blit(get_image(path + '\\animation\\label.png'), (0, 560))
        screen.blit(get_image(path + '\\animation\\coin_red.png'), ((tileRed[0] - 1)*50, (tileRed[1] - 1)*35+40))
        screen.blit(get_image(path + '\\animation\\coin_blue.png'), ((tileBlue[0] - 1)*50, (tileBlue[1] - 1)*35+40))
        for i in range(len(tiles)):
            screen.blit(get_image(path + '\\animation\\coin.png'), ((tiles[i][0] - 1)*50, (tiles[i][1] - 1)*35+40))

        p1.update(direction, screen)
        p2.update(direction, screen)
        for i in range(len(anims)):
        	anims[i].update(screen)

        for i in range(len(walls)):
            screen.blit(get_image(path + '\\animation\\thymbal.png'), ((walls[i][0] - 1)*50, (walls[i][1] - 1)*35+40))
        
        pygame.display.flip()
        clock.tick(60)

main()