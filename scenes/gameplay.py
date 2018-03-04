from super import SceneSuper
from player import *
from animator import *
from tile import *
from board import *
import random
import pygame
import os

class GameScene(SceneSuper):

    def __init__(self):
        SceneSuper.__init__(self)
        self.background = '/animation/bg_2.png'
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/..'
        self.board = Board()
        self.tiles = self.board.get_tiles("level2.txt");
        self.p1 = Player(self.path + '/animation/character1/', self.board.player1[0], self.board.player1[1])
        self.p2 = Player(self.path + '/animation/character2/', self.board.player2[0], self.board.player2[1])
        self.emptySpots = self.board.emptySpots
        self.animationSpots = []
        for x in range(4):
            rand1 = random.randint(0, len(self.emptySpots) - 1)
            self.animationSpots.append(self.emptySpots[rand1])
            del self.emptySpots[rand1]

        self.anims = [
            Animator(self.path + '/animation/coin/', self.animationSpots[0][0], self.animationSpots[0][1]),
            Animator(self.path + '/animation/dice2/', self.animationSpots[1][0], self.animationSpots[1][1]),
            Animator(self.path + '/animation/dice1/', self.animationSpots[2][0], self.animationSpots[2][1]),
            Animator(self.path + '/animation/pin2/', self.animationSpots[3][0], self.animationSpots[3][1])
        ]

    def handle_input(self, events, keys):
        pass

    def on_update(self):
        pass

    def on_render(self, screen, clock):
        done = False
        player_dead = False


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
        screen.blit(self.get_image(self.path + self.background), (0, 0))
        screen.blit(self.get_image(self.path + '/animation/label.png'), (0, 560))

        for i in range(len(self.tiles)):
            screen.blit(self.get_image(self.path + self.tiles[i].path), self.tiles[i].getRealXY())

        p1_status = self.p1.update(direction, screen, self.board)
        p2_status = self.p2.update(direction, screen, self.board)

        if p1_status == "dead" or p2_status == "dead":
            player_dead = True

        for i in range(len(self.anims)):
            self.anims[i].update(screen)

        pygame.display.flip()
        clock.tick(60)