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

pygame.init()
screen = pygame.display.set_mode((275, 275))
done = False
clock = pygame.time.Clock()

path = os.path.dirname(os.path.realpath(__file__))[:-6]
frame = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    frame += 1
    frame = (frame - 1) % 30 + 1

    screen.fill((255, 255, 255))
    
    screen.blit(get_image(path + '\\animation\\character1\\idle\\' + (4-len(str(frame)))*'0' + str(frame) + '.png'), (50, 100))
    screen.blit(get_image(path + '\\animation\\character2\\idle\\' + (4-len(str(frame)))*'0' + str(frame) + '.png'), (150, 100))
    
    pygame.display.flip()
    clock.tick(60)