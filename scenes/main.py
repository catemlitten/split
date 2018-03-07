import pygame
from menu import MenuScene
from super import SceneSuper

def play_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        filtered_events = [] # this is to track all events that are not quit events
        for event in pygame.event.get():
            quit_flag = False
            if event.type == pygame.QUIT:
                quit_flag = True
            elif event.type == pygame.KEYDOWN:
                if pressed_keys[pygame.K_p]:
                    print("pause")
                   # pause() # pause game on typing 'p'
                elif pressed_keys[pygame.K_q]:
                    quit_flag = True # quit game on typing 'q'
            if quit_flag:
                active_scene.abort()
            else:
                filtered_events.append(event)

        active_scene.handle_input(filtered_events, pressed_keys)
        active_scene.on_update()
        active_scene.on_render(screen, clock)

        active_scene = active_scene.next

      #  pygame.display.flip()
      #  clock.tick(fps)

play_game(800, 600, 60, MenuScene())
