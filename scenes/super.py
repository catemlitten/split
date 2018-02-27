class SceneSuper:

    def __init__(self):
        self.next = self

    def handle_input(self, events, keys):
        raise NotImplementedError("handle_input abstract method must be defined in subclass.")

    def on_update(self):
        raise NotImplementedError("on_update abstract method must be defined in subclass.")

    def on_render(self, screen):
        raise NotImplementedError("on_render abstract method must be defined in subclass.")

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def abort(self):
        self.switch_to_scene(None)