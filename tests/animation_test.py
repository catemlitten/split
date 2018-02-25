from player import *
from animator import *
from tile import *
from board import *
import random
import pygame
import os

_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    player_dead = False
    background = '/animation/bg_2.png'
    clock = pygame.time.Clock()
    path = os.path.dirname(os.path.realpath(__file__)) + '/..'

    direction = '-'
    board = Board()
    tiles = board.get_tiles("level2.txt");
    '''
    board object can be created here, and the parameter for the __init__ can be the level file at [path + '/levels/level1.txt']
    it can have check() to check if jumps are possible
    update() to edit tiles after a jump
    and getPlayerInitPos() so we can put the players in the right position initially. 
        #Maybe this can be an array like this [[9,6],[12,11]]
    '''

    p1 = Player(path + '/animation/character1/', board.player1[0], board.player1[1])
    p2 = Player(path + '/animation/character2/', board.player2[0], board.player2[1])
    '''
    Maybe this animation objects can be somehow part of the board? Think about later
     maybe make them randomly chosen from empty spaces
    '''
    emptySpots = board.emptySpots
    animationSpots = []
    for x in range(4):
        rand1 = random.randint(0, len(emptySpots) - 1)
        animationSpots.append(emptySpots[rand1])
        del emptySpots[rand1]

    anims = [	
    	Animator(path + '/animation/coin/', animationSpots[0][0], animationSpots[0][1]),
    	Animator(path + '/animation/dice2/', animationSpots[1][0], animationSpots[1][1]),
    	Animator(path + '/animation/dice1/', animationSpots[2][0], animationSpots[2][1]),
    	Animator(path + '/animation/pin2/', animationSpots[3][0], animationSpots[3][1])
    ]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if player_dead:
            background = '/animation/gameover.jpg'

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
        screen.blit(get_image(path + background), (0, 0))
        screen.blit(get_image(path + '/animation/label.png'), (0, 560))

        for i in range(len(tiles)):
            screen.blit(get_image(path + tiles[i].path), tiles[i].getRealXY())
       
        p1_status = p1.update(direction, screen, board)
        p2_status = p2.update(direction, screen, board)

        if p1_status == "dead" or p2_status == "dead":
            player_dead = True

        for i in range(len(anims)):
            anims[i].update(screen)

        pygame.display.flip()
        clock.tick(60)

main()