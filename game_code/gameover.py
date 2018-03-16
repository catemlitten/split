from super import SceneSuper
#from menu import MenuScene
from player import *
from animator import *
from tile import *
from board import *
import random
import pygame
import os

class GameOver(SceneSuper):

    def __init__(self, menuObject):
        SceneSuper.__init__(self)
        self.background = '/animation/gameover.png'
        self.menuObject = menuObject
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/..'
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (203, 209, 219)
        self.particles = []
        for i in range(35):
            self.particles.append([random.randrange(0, 800), random.randrange(0, 600), random.randrange(1, 6)])

    def handle_input(self, events, keys):
        pass

    def on_update(self):
        pass
    
    def button(self, text, posX, posY, width, height, active, inactive, screen, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (posX + width) > mouse[0] > posX and (posY + height) > mouse[1] > posY:
            pygame.draw.rect(screen, inactive, (posX, posY, width, height))
            if click[0] == 1 and action != None:
                if action != 'abort':
                    self.switch_to_scene(action)
                else:
                    self.abort()
        else:
            pygame.draw.rect(screen, active, (posX, posY, width, height))
            
        smallText = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "/PressStart2P-Regular.ttf", 10)
        midText = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "/PressStart2P-Regular.ttf", 70)
        largeText = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "/PressStart2P-Regular.ttf", 115)
        textSurf, textRect = self.text_objects(text, smallText)
        textRect.center = ((posX + (width / 2)), (posY + (height / 2)))
        screen.blit(textSurf, textRect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def on_render(self, screen, clock):
        frame = 0
        screen.fill((255, 255, 255))
        screen.blit(self.get_image(self.path + self.background), (0, 0))

        self.button("Play again?", 650, 250, 120, 50, self.white, self.gray, screen, self.menuObject)
        self.button("Quit", 650, 320, 120, 50, self.white, self.gray, screen, 'abort')

        if frame % 10 == 0:
            self.particles.append([random.randrange(0, 800), 610, random.randrange(1, 6)])

        for i in range(len(self.particles) - 1, -1, -1):
            pygame.draw.circle(screen, (249, 34, 45, 100), (self.particles[i][0], self.particles[i][1]), self.particles[i][2], 1)
            self.particles[i][1] -= self.particles[i][2]
            if self.particles[i][1] < -10:
                del self.particles[i]

        frame += 1
        pygame.display.flip()
        clock.tick(60)