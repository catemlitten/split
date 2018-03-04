import os
import pygame

class SceneSuper:
    _image_library = {}

    def __init__(self):
        self.next = self

    def handle_input(self, events, keys):
        raise NotImplementedError("handle_input abstract method must be defined in subclass.")

    def on_update(self):
        raise NotImplementedError("on_update abstract method must be defined in subclass.")

    def on_render(self, screen, clock):
        raise NotImplementedError("on_render abstract method must be defined in subclass.")

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def abort(self):
        self.switch_to_scene(None)
        pygame.quit()

    def get_image(self, path):
        global _image_library
        image = self._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
            image = pygame.image.load(canonicalized_path)
            self._image_library[path] = image
        return image