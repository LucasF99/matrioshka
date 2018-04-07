import pygame
import tiles
import textures
import random

class GameStateManager(object):

    def __init__(self, state, system, body, world, cloud):
        self.state = state
        self.system = system
        self.body = body
        self.world = world
        self.cloud = cloud

    def set_state(self, state):
        self.state = state

    def add_state(self, val):
        self.state += val

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

    def get_cloud(self):
        return self.cloud

########## States
# 0 - menu
# 1 - universe map
# 2 - system map
# 3 - planet / star screen
# 4 - cloud (isometric?)
####

class Drawer(object):

    def __init__(self, state_manager, data_manager, ui_manager, galaxy, screen):
        self.s_man = state_manager
        self.d_man = data_manager
        self.galaxy = galaxy
        self.screen = screen
        self.ui_man = ui_manager
        pygame.font.init()
        #self.font = pygame.font.SysFont('oratorstdopentype', 24)
        self.font = pygame.font.SysFont('arial', 24)

    def draw(self):
        if self.s_man.get_state() == 3:
            body = self.s_man.get_body()
            image = body.get_image()
            the_cloud = self.s_man.get_cloud()
            sphereimg = textures.img[0]

            limiting_dimension = self.screen.get_height()
            if self.screen.get_width() < self.screen.get_height():
                limiting_dimension = self.screen.get_width()

            image = pygame.transform.scale(image, (int(limiting_dimension*0.7), int(limiting_dimension*0.7)))
            sphereimg = pygame.transform.scale(sphereimg, (int(limiting_dimension*0.9), int(limiting_dimension*0.9)))
            image_rect = image.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            sphere_rect = sphereimg.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

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

        elif self.s_man.get_state() == 2:

            bodies = self.s_man.get_system().bodies
            num_bodies = len(bodies)

            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()

            total_w = 0
            current_w = 0

            for i in bodies:
                total_w += i.get_image().get_width()

            for i in range(num_bodies):
                image = bodies[i].get_image()
                w = image.get_width()
                h = image.get_height()
                x = 0.9*screen_w - 0.8*i*((screen_w-total_w)/num_bodies) - current_w
                y = screen_h/2
                rect = image.get_rect(midright=(x,y))
                self.screen.blit(image, rect)
                current_w += w

                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

                if mouse_x<=x and mouse_x>=x-w:
                    if mouse_y>=y-h/2 and mouse_y<=y+h/2:
                        self.ui_man.draw_text_box(bodies[i].get_name(), True, (10,10,10), (180,180,180), x+w/10, y-h/2)

        self.ui_man.draw()

class RandomEventManager(object):

    def __init__(self, state_manager, data_manager):
        self.s_man = state_manager
        self.d_man = data_manager

    def update(self):
        if random.randint(1,60) == 1: # make people randomly move into cloud
            self.d_man.add_value('money', self.d_man.price)
            self.d_man.add_value('storage', 10)
            self.s_man.get_cloud().add_population(10)
            random.choice(self.s_man.system.planets).add_population(-10)
            self.s_man.system.update_population()

class EventHandler(object):

    def __init__(self, state_manager, data_manager, ui_manager, galaxy, screen):
        self.s_man = state_manager
        self.d_man = data_manager
        self.galaxy = galaxy
        self.screen = screen
        self.ui_man = ui_manager

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            self.ui_man.check_button_pressed(pygame.mouse.get_pos())
