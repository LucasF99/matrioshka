import pygame
import tiles
import textures
import random
import buildings
import os

class GameStateManager(object):

    def __init__(self, state, system, body, world, cloud):
        self.state = state
        self.system = system
        self.body = body
        self.world = world
        self.cloud = cloud
        self.done = False

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

    def get_done(self):
        return self.done

    def set_done(self, value):
        self.done = value

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
        self.screen_w = screen.get_width()
        self.screen_h = screen.get_height()
        self.camera_x = self.screen_w/2
        self.camera_y = self.screen_h/2
        self.camera_zoom = 2

        self.dir = os.path.dirname(__file__)

        self.tile_surface = pygame.Surface((64,64))

        pygame.font.init()
        #self.font = pygame.font.SysFont('oratorstdopentype', 24)
        self.font = pygame.font.SysFont('arial', 24)
        limiting_dimension = self.screen.get_height()
        if self.screen.get_width() < self.screen.get_height():
            limiting_dimension = self.screen.get_width()
        self.body_view_size = int(limiting_dimension*0.7)

        self.img_test_red = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','test_red.png')),
                                                    (int(self.body_view_size/4), int(self.body_view_size/4)))

        self.update_tiles()

    def move_camera(self, move):
        self.camera_x += move[0]
        self.camera_y += move[1]

    def zoom_camera(self, zoom):
        if self.camera_zoom + zoom < 0.2:
            self.camera_zoom = 0.2
        else:
            self.camera_zoom += zoom

    def zoom_mult(self, value):
        self.camera_zoom *= value

    def update_tiles(self):
        tmap = self.s_man.get_world().get_tile_map()
        tw = tmap.get_tile_w()
        th = tmap.get_tile_h()

        self.surface = pygame.Surface((len(tmap.map)*th, len(tmap.map[0])*tw))

        images = []

        for i in range(len(tiles.images)):
            images.append(tiles.images[i])

        for i in range(len(tmap.map)):
            for j in range(len(tmap.map[i])):
                x = i * tw
                y = j * th
                image = images[tmap.map[i][j]]
                image_rect = image.get_rect(topleft = (x, y))
                self.surface.blit(image, image_rect)

    def draw(self):
        if self.s_man.get_state() == 3:
            body = self.s_man.get_body()
            if body.get_type() == 'star':
                image = body.get_image()
                the_cloud = self.s_man.get_cloud()
                sphereimg = textures.img[0]

                image = pygame.transform.scale(image, (self.body_view_size, self.body_view_size))
                sphereimg = pygame.transform.scale(sphereimg, (int(self.body_view_size*1.3), int(self.body_view_size*1.3)))
                image_rect = image.get_rect(center=(self.screen_w/2, self.screen_h/2))
                sphere_rect = sphereimg.get_rect(center=(self.screen_w/2, self.screen_h/2))

                self.screen.blit(image, image_rect)
                self.screen.blit(sphereimg, sphere_rect)

                if body.get_energy_level() == 1:
                    upgrade_img = pygame.transform.scale(body.upgrade_img, (int(self.body_view_size*0.3),int(self.body_view_size*0.3)))
                    upgrade_rect = upgrade_img.get_rect(center=(self.screen_w/2, self.screen_h/2))
                    self.screen.blit(upgrade_img, upgrade_rect)

            elif body.get_type() == 'planet':
                image = body.get_image()
                the_cloud = self.s_man.get_cloud()

                limiting_dimension = self.screen.get_height()
                if self.screen.get_width() < self.screen.get_height():
                    limiting_dimension = self.screen.get_width()

                build_select = body.check_mouse((pygame.mouse.get_pos()[0]-self.screen_w/2,
                                                pygame.mouse.get_pos()[1]-self.screen_h/2), self.body_view_size/2)

                image = pygame.transform.scale(image, (int(limiting_dimension*0.7), int(limiting_dimension*0.7)))
                image_rect = image.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

                self.screen.blit(image, image_rect)

                for i in range(8):
                    if body.buildings[i] == 1:
                        build_rect = self.img_test_red.get_rect(center=(body.building_coords[i][0]*self.body_view_size/2+self.screen_w/2,
                                                                    body.building_coords[i][1]*self.body_view_size/2+self.screen_h/2))
                        self.screen.blit(self.img_test_red, build_rect)

                if build_select[0] != None:
                    sel_rect = self.img_test_red.get_rect(center=(build_select[0]+self.screen_w/2,build_select[1]+self.screen_h/2))
                    self.screen.blit(self.img_test_red, sel_rect)

        elif self.s_man.get_state() == 4:

#            tmap = self.s_man.get_world().get_tile_map()
#            tw = tmap.get_tile_w()
#            th = tmap.get_tile_h()
#
#            images = []
#
#            for i in range(len(tiles.images)):
#                images.append(pygame.transform.scale(tiles.images[i], (int(tw*self.camera_zoom), int(th*self.camera_zoom))))
#
#            for i in range(len(tmap.map)):
#                for j in range(len(tmap.map[i])):
#                    x = self.camera_x - self.screen_w/2 + i * tw * self.camera_zoom
#                    y = self.camera_y - self.screen_h/2 + j * th * self.camera_zoom
#                    image = pygame.transform.scale(images[tmap.map[i][j]], (int(tw*self.camera_zoom), int(th*self.camera_zoom)))
#                    image_rect = image.get_rect(topleft = (x, y))
#                    self.screen.blit(image, image_rect)
#
            x = self.camera_x - self.screen_w/2
            y = self.camera_y - self.screen_h/2
            surf = pygame.transform.scale(self.surface, (int(self.camera_zoom*self.surface.get_width()), int(self.camera_zoom*self.surface.get_height())))
            self.screen.blit(surf, (x, y))

        elif self.s_man.get_state() == 5:

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
                        if pygame.mouse.get_pressed()[0]:
                            self.s_man.set_body(bodies[i])
                            self.s_man.set_state(3)

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

    def __init__(self, state_manager, data_manager, ui_manager, build_manager, drawer, galaxy, screen):
        self.s_man = state_manager
        self.d_man = data_manager
        self.b_man = build_manager
        self.galaxy = galaxy
        self.screen = screen
        self.screen_w = screen.get_width()
        self.screen_h = screen.get_height()
        self.ui_man = ui_manager
        self.drawer = drawer
        self.world = self.s_man.get_world()
        self.last_mouse_x = 0
        self.last_mouse_y = 0

    def update(self):
    #    if pygame.mouse.get_pressed()[0]:
    #        self.ui_man.check_button_pressed(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.ui_man.check_button_pressed(pygame.mouse.get_pos()) # check buttons
                if self.s_man.get_state() == 3 and self.s_man.get_body().get_type() == 'planet':
                    build_index = self.s_man.get_body().check_mouse((pygame.mouse.get_pos()[0]-self.drawer.screen_w/2,
                                                    pygame.mouse.get_pos()[1]-self.drawer.screen_h/2), self.drawer.body_view_size/2)[2]
                    if build_index != None:         # build
                        self.s_man.get_body().buildings[build_index] = 1
                        self.b_man.add('mines', buildings.Mine())
                if self.s_man.get_state() == 4: # build tiles
                    index = self.s_man.get_world().get_tile_map().get_index(
                                        pygame.mouse.get_pos(), (self.drawer.camera_x, self.drawer.camera_y),
                                        self.drawer.camera_zoom, (self.screen_w, self.screen_h))
                    self.b_man.build_tile(self.world, index, 1)
                    self.drawer.update_tiles()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.drawer.zoom_mult(2)
                elif event.button == 5:
                    self.drawer.zoom_mult(0.5)
            if event.type == pygame.QUIT:
                self.s_man.set_done(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.s_man.set_done(True)
                if event.key == pygame.K_UP and self.s_man.get_state()<4:
                    self.s_man.add_state(1)
                if event.key == pygame.K_DOWN and self.s_man.get_state()>2:
                    self.s_man.add_state(-1)
            if self.s_man.get_state() == 4:
                if pygame.mouse.get_pressed()[0]:
                    self.drawer.move_camera((- self.last_mouse_x + pygame.mouse.get_pos()[0], - self.last_mouse_y + pygame.mouse.get_pos()[1]))

            self.last_mouse_x = pygame.mouse.get_pos()[0]
            self.last_mouse_y = pygame.mouse.get_pos()[1]
