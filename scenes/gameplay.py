from super import SceneSuper
from gameover import GameOver
from player import *
from animator import *
from tile import *
from board import *
import random
import pygame
import os

class GameScene(SceneSuper):

    def __init__(self, level, background):
        SceneSuper.__init__(self)
        self.background = background
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/..'
        self.board = Board()
        self.tiles = self.board.get_tiles(level);
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
        self.particles = []
        for i in range(35):
            self.particles.append([random.randrange(0, 800), random.randrange(0, 600), random.randrange(1, 6)])
        self.fallingCoins = []

    def set_tiles(self, level):
        self.tiles = self.board.get_tiles(level)

    def get_background(self):
        return self.background

    def set_background(self, image):
        self.background = image
    
    def handle_input(self, events, keys):
        pass

    def on_update(self):
        pass

    def on_render(self, screen, clock):
        frame = 0

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

        if p1_status[0] == "dead" or p2_status[0] == "dead":
            self.switch_to_scene(GameOver())
        if p1_status[0] == "moving":
            print("drop tile player 1")
            if frame % 60 == 0:
                fallingCoin = Animator(self.path + '/animation/coin/', p1_status[1], p1_status[2])
                fallingCoin.realX += 12.5
                fallingCoin.realY += 30
                self.fallingCoins.append([fallingCoin, 0])
            for i in range(len(self.fallingCoins) - 1, -1, -1):
                self.fallingCoins[i][1] += 0.3
                self.fallingCoins[i][0].realY += self.fallingCoins[i][1]
                self.fallingCoins[i][0].update(screen)
                if self.fallingCoins[i][0].realY > 600:
                    del self.fallingCoins[i]
        if p2_status[0] == "moving":
            print("drop tile player 2")

        if frame % 10 == 0:
            self.particles.append([random.randrange(0, 800), 610, random.randrange(1, 6)])

        for i in range(len(self.particles) - 1, -1, -1):
            pygame.draw.circle(screen, (255, 255, 255, 100), (self.particles[i][0], self.particles[i][1]), self.particles[i][2], 1)
            self.particles[i][1] -= self.particles[i][2]
            if self.particles[i][1] < -10:
                del self.particles[i]

        for i in range(len(self.anims)):
            self.anims[i].update(screen)

        frame += 1
        pygame.display.flip()
        clock.tick(60)
