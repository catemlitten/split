import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
light_red = (100, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

smallText = pygame.font.Font("freesansbold.ttf", 15)
midText = pygame.font.Font("freesansbold.ttf", 70)
largeText = pygame.font.Font("freesansbold.ttf", 115)

display_width = 800
display_height = 600

FPS = 30
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Split")

screenImg = pygame.image.load("SplitMenuScreen.png")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitGame():
    pygame.quit()
    quit()
    
def button(text, posX, posY, width, height, active, inactive, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
            
    if (posX + width) > mouse[0] > posX and (posY + height) > mouse[1] > posY:
        pygame.draw.rect(gameDisplay, inactive, (posX, posY, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, active, (posX, posY, width, height))

    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((posX +(width/2)), (posY + (height/2)))
    gameDisplay.blit(textSurf, textRect)
    
def setBackground(posX, posY):
    gameDisplay.blit(screenImg, (posX, posY))

def gameMenu():

    Menu = True
    
    while Menu:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        setBackground(0,0)
        
        button("Start Game", 650, 190, 100, 50, red, light_red, gameLoop)
        button("Level Select", 650, 250, 100, 50, red, light_red)
        button("Options", 650, 310, 100, 50, red, light_red)
        button("Quit Game", 650, 370, 100, 50, red, light_red, quitGame)

        pygame.display.update()
        


block_size = 10
block_height = 10
block_width = 10
FPS = 40

def snake(block_size, snakeList):
    for XnY in snakeList:
        rect = pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    
def gameLoop():

    gameExit = False
    gameOver = False

    snakeList = []
    
    x = random.randrange(0,display_width - block_size)
    y = random.randrange(0,display_height - block_size)

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    new_x = 0
    new_y = 0
    
    while not gameExit:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_y_change = 0
                    lead_x_change = -(block_size)
                elif event.key == pygame.K_RIGHT:
                    lead_y_change = 0
                    lead_x_change = block_size
                elif event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -(block_size)
                elif event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = block_size

        lead_x += lead_x_change
        lead_y += lead_y_change


        gameDisplay.fill(white)
        rect = pygame.draw.rect(gameDisplay, green, [lead_x,lead_y,block_height,block_width])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(block_size, snakeList)
        
        circle = pygame.draw.circle(gameDisplay, red, (x,y), 5, 0)
        pygame.display.update()
           
        if rect.colliderect(circle):
            
            x = random.randrange(0,display_width)
            y = random.randrange(0,display_height)
            pygame.display.update()
            pygame.display.flip()

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameExit = True
            pygame.display.update()

        clock.tick(FPS)
        
    pygame.quit
    quit()


gameMenu()
