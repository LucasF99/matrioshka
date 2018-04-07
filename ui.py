import pygame
import os

class UIManager(object):

    def __init__(self, state_manager, data_manager, screen):
        self.s_man = state_manager
        self.d_man = data_manager
        self.screen = screen
        pygame.font.init()
        #self.font = pygame.font.SysFont('oratorstdopentype', 24)
        self.font = pygame.font.SysFont('arial', int(0.03*screen.get_height()))
        self.dir = os.path.dirname(__file__)
        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','system_icon.png')),
                                                  (64*int(self.screen.get_height()/320), 64*int(self.screen.get_height()/320)))) # index 0

        self.init_buttons()

    def init_buttons(self):
        self.buttons = []
        for i in range(5):
            self.buttons.append([])

        #system view button
        img_sys_view = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','system_icon.png')),
                                                  (64*int(self.screen.get_height()/320), 64*int(self.screen.get_height()/320)))
        def func_sys_view():
            self.s_man.set_state(2)

        self.buttons[3].append((0, int(self.screen.get_height()*0.055), 64*int(self.screen.get_height()/320), 64*int(self.screen.get_height()/320), img_sys_view, func_sys_view)) # x, y, w, h, img, func
        #self.buttons[2].append((100, int(self.screen.get_height()*0.055), 64*int(self.screen.get_height()/320), 64*int(self.screen.get_height()/320), img_sys_view, func_sys_view)) # x, y, w, h, img, func

    def draw(self):
        if self.s_man.get_state() == 3:

            body = self.s_man.get_body()
            the_cloud = self.s_man.get_cloud()

            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            color = (200,200,200)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, 0, screen_w, screen_h*0.05))

            color = (100,100,100)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h*0.05, screen_w, screen_h*0.005))

            text_surface = self.font.render("Energy: %5d/%5d    Storage: %5d/%5d    Money: %5d    System Population: %8d    Cloud Population: %8d"%(self.d_man.get_value('energy'),
                                            self.d_man.get_value('max_energy'),self.d_man.get_value('storage'),
                                            self.d_man.get_value('max_storage'),self.d_man.get_value('money'),
                                            body.system.get_population(),the_cloud.get_population()),
                                            True, (0,0,0))

            self.screen.blit(text_surface, (16, 10))

        for i in self.buttons[self.s_man.get_state()]:
            rect = i[4].get_rect(topleft=(i[0], i[1]))
            self.screen.blit(i[4],rect)
            ## TODO: run func (i[5]) when clicked (do this in eventhandler)

    def check_button_pressed(self, pos):
        for b in self.buttons[self.s_man.get_state()]:
            print(str(b))
            if pos[0] >= b[0] and pos[0] <= b[0]+b[2]:
                if pos[1] >= b[1] and pos[1] <= b[0]+b[3]:
                    b[5]()


    def draw_text_box(self, text, antialias, color, background, x, y):
        #text_box = self.font.render(text, antialias, color, background)
        text_box = self.font.render(text, antialias, color, background)
        self.screen.blit(text_box, (x,y))
