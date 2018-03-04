from super import SceneSuper
import pygame
from gameplay import GameScene

class MenuScene(SceneSuper):

    def __init__(self):
        SceneSuper.__init__(self)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.light_red = (100, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.screenImg = pygame.image.load("SplitMenuScreen.png")

    def handle_input(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                #change scene
                self.switch_to_scene(GameScene())

    def on_update(self):
        pass

    def setBackground(self, posX, posY, screen):
        screen.blit(self.screenImg, (posX, posY))

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

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
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        midText = pygame.font.Font("freesansbold.ttf", 70)
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = self.text_objects(text, smallText)
        textRect.center = ((posX + (width / 2)), (posY + (height / 2)))
        screen.blit(textSurf, textRect)

    def on_render(self, screen, clock):
        self.setBackground(0, 0, screen)

        self.button("Start Game", 650, 190, 100, 50, self.red, self.light_red, screen, GameScene())
        self.button("Level Select", 650, 250, 100, 50, self.red, self.light_red, screen)
        self.button("Options", 650, 310, 100, 50, self.red, self.light_red, screen)
        self.button("Quit Game", 650, 370, 100, 50, self.red, self.light_red, screen, 'abort')
        pygame.display.flip()
        clock.tick(60)