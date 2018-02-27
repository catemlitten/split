from super import SceneSuper

class GameScene(SceneSuper):

    def __init__(self):
        SceneSuper.__init__(self)

    def handle_input(self, events, keys):
        pass

    def on_update(self):
        pass

    def on_render(self, screen):
        screen.fill((0, 0, 255))