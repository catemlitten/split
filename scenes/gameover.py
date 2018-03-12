from super import SceneSuper
from player import *
from animator import *
from tile import *
from board import *
import random
import pygame
import os

class GameOver(SceneSuper):

    def __init__(self):
        SceneSuper.__init__(self)
        self.background = '/animation/gameoverwide.jpg'
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/..'
        self.particles = []
        for i in range(35):
            self.particles.append([random.randrange(0, 800), random.randrange(0, 600), random.randrange(1, 6)])

    def handle_input(self, events, keys):
        pass

    def on_update(self):
        pass

    def on_render(self, screen, clock):
        frame = 0
        screen.fill((255, 255, 255))
        screen.blit(self.get_image(self.path + self.background), (0, 0))

        if frame % 10 == 0:
            self.particles.append([random.randrange(0, 800), 610, random.randrange(1, 6)])

        for i in range(len(self.particles) - 1, -1, -1):
            pygame.draw.circle(screen, (255, 255, 255, 100), (self.particles[i][0], self.particles[i][1]), self.particles[i][2], 1)
            self.particles[i][1] -= self.particles[i][2]
            if self.particles[i][1] < -10:
                del self.particles[i]

        frame += 1
        pygame.display.flip()
        clock.tick(60)