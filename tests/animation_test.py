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

def drawFrame(sc, path, frame, x, y):
    f = str(frame)
    sc.blit(get_image(path + (4-len(f))*'0' + f + '.png'), (x,y))

def move(f, moving):
    frames = f[:]
    if frames[0][0] == 0:
        moving = True
        frames[0][0] = 1
        frames[3][0] = 0
    if frames[1][0] == 0:
        moving = True
        frames[1][0] = 1
        frames[4][0] = 0
    return frames, moving

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    clock = pygame.time.Clock()

    path = os.path.dirname(os.path.realpath(__file__)) + '\\..'
    frames = [[0,27],[0,27],[0,60],[0,30],[0,30],[0,60],[0,60],[0,60]]

    x1 = 187.5
    y1 = 150
    x2 = 337.5
    y2 = 150
    direction = '-'
    moving = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if pygame.key.get_pressed()[pygame.K_w] and not moving:
            direction = 'w'
            frames, moving  = move(frames, moving)
        elif pygame.key.get_pressed()[pygame.K_a] and not moving:
            direction = 'a'
            frames, moving = move(frames, moving)
        elif pygame.key.get_pressed()[pygame.K_s] and not moving:
            direction = 's'
            frames, moving = move(frames, moving)
        elif pygame.key.get_pressed()[pygame.K_d] and not moving:
            direction = 'd'
            frames, moving = move(frames, moving)
    
        for i in range(len(frames)):
            if frames[i][0] > 0:
                frames[i][0] += 1
                if frames[i][0] > frames[i][1]:
                    frames[i][0] = 0 
                    if i == 0 or i == 1:
                        direction = '-'
                        moving  = False
        if frames[2][0] == 0:
            frames[2][0] = 1
        if frames[5][0] == 0:
            frames[5][0] = 1
        if frames[6][0] == 0:
            frames[6][0] = 1
        if frames[7][0] == 0:
            frames[7][0] = 1
        if frames[3][0] == 0 and frames[0][0] == 0:
            frames[3][0] = 1
        if frames[4][0] == 0 and frames[1][0] == 0:
            frames[4][0] = 1

        tiles = [[2,5],[2,6],[3,6],[4,6],[5,6],[5,5],[6,6],[7,6]]
        screen.fill((255, 255, 255))
        screen.blit(get_image(path + '\\animation\\bg.png'), (0, 0))
        for i in range(len(tiles)):
            screen.blit(get_image(path + '\\animation\\tile.png'), (tiles[i][0]*50+100, tiles[i][1]*35+20))
        
        if direction == 'w':
            y1 -= (35/26)
            y2 -= (35/26)
        elif direction == 'a':
            x1 -= (50/26)
            x2 -= (50/26)
        elif direction == 's':
            y1 += (35/26)
            y2 += (35/26)
        elif direction == 'd':
            x1 += (50/26)
            x2 += (50/26)

        if frames[0][0] > 0:
            drawFrame(screen, path + '\\animation\\character1\\jump\\', frames[0][0], x1, y1)
        if frames[1][0] > 0:
            drawFrame(screen, path + '\\animation\\character2\\jump\\', frames[1][0], x2, y2)
        if frames[2][0] > 0:
            drawFrame(screen, path + '\\animation\\dice1\\', frames[2][0], 150, 400)
        if frames[3][0] > 0:
            drawFrame(screen, path + '\\animation\\character1\\idle\\', frames[3][0], x1, y1)
        if frames[4][0] > 0:
            drawFrame(screen, path + '\\animation\\character2\\idle\\', frames[4][0], x2, y2)
        if frames[5][0] > 0:
            drawFrame(screen, path + '\\animation\\dice2\\', frames[5][0], 600, 200)
        if frames[6][0] > 0:
            drawFrame(screen, path + '\\animation\\pin1\\', frames[6][0], 100, 100)
        if frames[7][0] > 0:
            drawFrame(screen, path + '\\animation\\pin2\\', frames[7][0], 550, 450)

        
        pygame.display.flip()
        clock.tick(60)

main()