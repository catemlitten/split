from player import *
from animator import *
from tile import *
from board import *
import random
import pygame
import os
import random

_image_library = {}
_sound_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    player_dead = False
    background = '/animation/bg_2.png'
    clock = pygame.time.Clock()
    path = os.path.dirname(os.path.realpath(__file__)) + '/..'

    direction = '-'


    #board object can be created here, and the parameter for the __init__ can be the level file at [path + '/levels/level1.txt']
    #it can have check() to check if jumps are possible
    #update() to edit tiles after a jump. Should return the index of the tile to be removed.

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

    	Animator(path + '/animation/pin1/', 9, 3),
    	Animator(path + '/animation/dice2/', 3, 12),
    	Animator(path + '/animation/dice1/', 14, 4),
    	Animator(path + '/animation/pin2/', 12, 9)
    ]

    #Of course, this list won't be hard-coded, and will instead come from board.getTiles()
    tiles = [
        Tile('/animation/coin.png', 3, 3),
        Tile('/animation/thymbal.png', 4, 3),
        Tile('/animation/coin.png', 5, 3),
        Tile('/animation/coin.png', 6, 3),
        Tile('/animation/thymbal.png', 3, 4),
        Tile('/animation/coin.png', 4, 4),
        Tile('/animation/coin.png', 5, 4),
        Tile('/animation/coin.png', 6, 4),
        Tile('/animation/coin.png', 3, 5),
        Tile('/animation/coin.png', 4, 5),
        Tile('/animation/coin_red.png', 6, 5),
        Tile('/animation/coin.png', 3, 6),
        Tile('/animation/coin.png', 4, 6),
        Tile('/animation/coin.png', 7, 6),
        Tile('/animation/coin.png', 8, 6),
        Tile('/animation/coin.png', 9, 6),
        Tile('/animation/thymbal.png', 3, 7),
        Tile('/animation/coin.png', 4, 7),
        Tile('/animation/coin.png', 7, 7),
        Tile('/animation/coin.png', 8, 7),
        Tile('/animation/thymbal.png', 9, 7),
        Tile('/animation/coin.png', 3, 8),
        Tile('/animation/coin.png', 4, 8),
        Tile('/animation/coin.png', 5, 8),
        Tile('/animation/coin.png', 6, 8),
        Tile('/animation/coin.png', 7, 8),
        Tile('/animation/coin.png', 8, 8),
        Tile('/animation/thymbal.png', 10, 11),
        Tile('/animation/coin.png', 11, 11),
        Tile('/animation/coin.png', 12, 11),
        Tile('/animation/coin.png', 13, 11),
        Tile('/animation/coin.png', 14, 11),
        Tile('/animation/coin_blue.png', 5, 12),
        Tile('/animation/coin.png', 6, 12),
        Tile('/animation/thymbal.png', 7, 12),
        Tile('/animation/thymbal.png', 10, 12),
        Tile('/animation/coin.png', 11, 12),
        Tile('/animation/coin.png', 12, 12),
        Tile('/animation/coin.png', 13, 12),
        Tile('/animation/coin.png', 14, 12),
        Tile('/animation/coin.png', 6, 13),
        Tile('/animation/coin.png', 7, 13),
        Tile('/animation/coin.png', 8, 13),
        Tile('/animation/coin.png', 9, 13),
        Tile('/animation/coin.png', 10, 13),
        Tile('/animation/coin.png', 11, 13),
        Tile('/animation/coin.png', 12, 13),
        Tile('/animation/coin.png', 13, 13),
        Tile('/animation/coin.png', 14, 13)
    ]

    fallingCoins = []
    particles = []
    for i in range(35):
        particles.append([random.randrange(0,800),random.randrange(0,600),random.randrange(1,6)])
    
    frame = 0

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

        #TO BE REPLACED: code for a tile getting deleted. Falling coin.
        if frame % 60 == 0:
            r = random.randrange(0,len(tiles))
            if tiles[r].path == '/animation/coin.png':
                fallingCoin = Animator(path + '/animation/coin/', tiles[r].x, tiles[r].y)
                fallingCoin.realX += 12.5
                fallingCoin.realY += 30
                fallingCoins.append([fallingCoin, 0])
                del tiles[r]
                play_sound(path + '/sounds/coinflip.wav')
                #print(fallingCoins)

        for i in range(len(fallingCoins)-1,-1,-1):
            fallingCoins[i][1] += 0.3
            fallingCoins[i][0].realY += fallingCoins[i][1]
            fallingCoins[i][0].update(screen)
            if fallingCoins[i][0].realY > 600:
                del fallingCoins[i]
                #print(fallingCoins)

        if frame % 10 == 0:
            particles.append([random.randrange(0,800),610,random.randrange(1,6)])

        for i in range(len(particles)-1,-1,-1):
            pygame.draw.circle(screen, (255,255,255,100), (particles[i][0], particles[i][1]), particles[i][2], 1)
            particles[i][1] -= particles[i][2]
            if particles[i][1] < -10:
                del particles[i]
       
        p1_status = p1.update(direction, screen, board)
        p2_status = p2.update(direction, screen, board)

        if p1_status == "dead" or p2_status == "dead":
            player_dead = True

        for i in range(len(anims)):
            anims[i].update(screen)


        frame += 1
        pygame.display.flip()
        clock.tick(60)

main()