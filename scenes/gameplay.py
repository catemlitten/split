from super import SceneSuper
from player import *
from animator import *
from tile import *
from board import *
import random
import pygame
import os

class GameScene(SceneSuper):


    def get_image(self, path):
        global _image_library
        image = self._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
            image = pygame.image.load(canonicalized_path)
            self._image_library[path] = image
        return image

    def __init__(self):
        SceneSuper.__init__(self)
        self._image_library = {}

    def handle_input(self, events, keys):
        pass

    def on_update(self):
        pass

    def on_render(self, screen):
        done = False
        player_dead = False
        background = '/animation/bg_2.png'
        path = os.path.dirname(os.path.realpath(__file__)) + '/..'
        board = Board()
        tiles = board.get_tiles("level2.txt");
        p1 = Player(path + '/animation/character1/', board.player1[0], board.player1[1])
        p2 = Player(path + '/animation/character2/', board.player2[0], board.player2[1])
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
        screen.blit(self.get_image(path + background), (0, 0))
        screen.blit(self.get_image(path + '/animation/label.png'), (0, 560))

        for i in range(len(tiles)):
            screen.blit(self.get_image(path + tiles[i].path), tiles[i].getRealXY())

        p1_status = p1.update(direction, screen, board)
        print(p1_status)
        p2_status = p2.update(direction, screen, board)

        if p1_status == "dead" or p2_status == "dead":
            player_dead = True

        for i in range(len(anims)):
            anims[i].update(screen)