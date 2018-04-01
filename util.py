import pygame

class GameStateManager(object):

    def __init__(self, state, system, body):
        self.state = state
        self.system = system
        self.body = body

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_system(self, system):
        self.system = system

    def get_system(self):
        return self.system

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

########## States
# 0 - menu
# 1 - universe map
# 2 - system map
# 3 - planet / star screen
# 4 - cloud (isometric?)
####

class Drawer(object):

    def __init__(self, state_manager, galaxy, screen):
        self.s_man = state_manager
        self.galaxy = galaxy
        self.screen = screen

    def draw(self):
        if self.s_man.get_state() == 3:
            image = self.s_man.get_body().get_image()

            limiting_dimension = self.screen.get_height()
            if self.screen.get_width() < self.screen.get_height():
                limiting_dimension = self.screen.get_width()

            image = pygame.transform.scale(image, (int(limiting_dimension*0.7), int(limiting_dimension*0.7)))
            image_rect = image.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

            self.screen.blit(image, image_rect)
