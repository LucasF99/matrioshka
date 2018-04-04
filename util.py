import pygame
import tiles
import textures

class GameStateManager(object):

    def __init__(self, state, system, body, world):
        self.state = state
        self.system = system
        self.body = body
        self.world = world

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

    def set_world(self, world):
        self.world = world

    def get_world(self):
        return self.world

########## States
# 0 - menu
# 1 - universe map
# 2 - system map
# 3 - planet / star screen
# 4 - cloud (isometric?)
####

class Drawer(object):

    def __init__(self, state_manager, data_manager, galaxy, screen):
        self.s_man = state_manager
        self.d_man = data_manager
        self.galaxy = galaxy
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.SysFont('oratorstdopentype', 24)

    def draw(self):
        if self.s_man.get_state() == 3:
            image = self.s_man.get_body().get_image()
            sphereimg = textures.img[0]

            limiting_dimension = self.screen.get_height()
            if self.screen.get_width() < self.screen.get_height():
                limiting_dimension = self.screen.get_width()

            image = pygame.transform.scale(image, (int(limiting_dimension*0.7), int(limiting_dimension*0.7)))
            sphereimg = pygame.transform.scale(sphereimg, (int(limiting_dimension*0.9), int(limiting_dimension*0.9)))
            image_rect = image.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            sphere_rect = sphereimg.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))


            text_surface = self.font.render("══╣Energy: %5d/%5d╠═══╣Storage: %5d/%5d╠══"%(self.d_man.get_value('energy'),
                                            self.d_man.get_value('max_energy'),self.d_man.get_value('storage'),
                                            self.d_man.get_value('max_storage')), False, (255,255,255))

            self.screen.blit(text_surface, (16, 16))
            self.screen.blit(image, image_rect)
            self.screen.blit(sphereimg, sphere_rect)

        elif self.s_man.get_state() == 4:

            start_x = 0
            start_y = self.screen.get_height()/2
            start_pos = (start_x, start_y)

            tmap = self.s_man.get_world().get_tile_map()
            tw = tmap.get_tile_w()
            th = tmap.get_tile_h()

            for i in range(len(tmap.map)):
                for j in reversed(range(len(tmap.map[i]))):
                    x = start_x + (tw/2)*(i+j)
                    y = start_y + (th/2)*(j-i)
                    image = tiles.images[tmap.map[i][j]]
                    image_rect = image.get_rect(bottomleft=(x,y+th/2))
                    self.screen.blit(image, image_rect)
