import pygame
import os

class UIManager(object):

    def __init__(self, state_manager, data_manager, screen):
        self.s_man = state_manager
        self.d_man = data_manager
        self.screen = screen
        pygame.font.init()
        #self.font = pygame.font.SysFont('oratorstdopentype', 24)
        #self.font = pygame.font.SysFont('arial', int(0.03*screen.get_height()))
        self.dir = os.path.dirname(__file__)
        self.font = pygame.font.Font(os.path.join(self.dir, 'res', 'font', 'novem___.ttf'), int(0.03*screen.get_height()))
        self.images = []
        self.scl = int(self.screen.get_height()/480)
        #self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','system_icon.png')),
        #                                          (64*self.scl, 64*self.scl))) # index 0

        # images
        self.img_sys_view = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','system_icon.png')),
                                                  (64*self.scl, 64*self.scl))
        self.img_gal_view = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','galaxy_icon.png')),
                                                (64*self.scl, 64*self.scl))
        self.img_cloud_icon = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','cloud_icon.png')),
                                                (64*self.scl, 64*self.scl))
        self.img_test_icon = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','test_icon.png')),
                                                (64*self.scl, 64*self.scl))
        self.img_build_icon = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','build_icon.png')),
                                                (64*self.scl, 64*self.scl))
        self.img_energy_upgrade_icon = pygame.transform.scale(pygame.image.load(os.path.join(self.dir,'res','energy_upgrade_icon.png')),
                                                (64*self.scl, 64*self.scl))

        self.init_elements()
        self.init_buttons()

    # button functions
    def state_change(self, s):
        self.s_man.set_state(s)

    def show_hide_button(self, b):
        if b[5]:
            b[5] = False
        else:
            b[5] = True

    def show_hide_element(self, e):
        if e.get_shown():
            e.set_shown(False)
        else:
            e.set_shown(True)

    def init_elements(self):
        self.elements = []
        for i in range(5):
            self.elements.append([])

        build_menu = Element(self, False)

        self.elements[3].append(build_menu)
        self.elements[2].append(self.elements[3][0])

    def run_body_relative_func(self, args):
        # args: [state manager, 'func', args]
        print("rel body: " + str(args[0].get_body()))
        getattr(args[0].get_body(), args[1])(args[2])

    def init_buttons(self):
        self.buttons = []
        for i in range(5):
            self.buttons.append([])

        self.buttons[3].append((0, int(self.screen.get_height()*0.055), 64*self.scl, 64*self.scl, self.img_sys_view, True, self.state_change, 2)) # [3][0] # x, y, w, h, img, show, func, args
        self.buttons[2].append((0, int(self.screen.get_height()*0.055), 64*self.scl, 64*self.scl, self.img_gal_view, True, self.state_change, 1)) # [2][0]
        self.buttons[1].append((0, int(self.screen.get_height()*0.055)+64*self.scl, 64*self.scl, 64*self.scl, self.img_cloud_icon, True, self.state_change, 4)) # [1][0]
        self.buttons[2].append(self.buttons[1][0])  # [2][1]
        self.buttons[3].append(self.buttons[1][0])  # [3][1]
        self.buttons[2].append((0, int(self.screen.get_height()*0.055)+2*64*self.scl, 64*self.scl, 64*self.scl, self.img_build_icon, True, self.show_hide_element, self.elements[3][0])) # [2][2]
        self.buttons[3].append(self.buttons[2][2])  # [3][2]
        self.buttons[4].append(self.buttons[3][0])  # [4][0]
        #self.buttons[2].append((100, int(self.screen.get_height()*0.055), 64*int(self.screen.get_height()/320), 64*int(self.screen.get_height()/320), img_sys_view, func_sys_view)) # x, y, w, h, img, func

    def draw(self):
        if self.s_man.get_state() == 3:

            body = self.s_man.get_body()
            the_cloud = self.s_man.get_cloud()

            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            color = (200,200,200)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, 0, screen_w, screen_h*0.05*2))
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h-screen_h*0.05, screen_w, screen_h*0.05))

            color = (100,100,100)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h*0.05, screen_w, screen_h*0.005))
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h*0.05*2, screen_w, screen_h*0.005))

            color = (240, 240, 240)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h-screen_h*0.055+1, screen_w, screen_h*0.005))

            text_surface = self.font.render("Energy: %5d/%5d    Storage: %5d/%5d    Money: %5d"%(self.d_man.get_value('energy'),
                                            self.d_man.get_value('max_energy'),self.d_man.get_value('storage'),
                                            self.d_man.get_value('max_storage'),self.d_man.get_value('money')),
                                            True, (0,0,0))
            text_2 = self.font.render("System Population: %8d    Cloud Population: %8d"%(body.system.get_population(),the_cloud.get_population()), True, (0,0,0))

            self.screen.blit(text_surface, (16, 14))
            self.screen.blit(text_2, (140, 72))

        elif self.s_man.get_state() == 2:
            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            color = (200,200,200)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, 0, screen_w, screen_h*0.05))
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h-screen_h*0.05, screen_w, screen_h*0.05))

            color = (100,100,100)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h*0.05, screen_w, screen_h*0.005))

            color = (240, 240, 240)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h-screen_h*0.055+1, screen_w, screen_h*0.005))

        elif self.s_man.get_state() == 4:
            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            color = (200,200,200)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, 0, screen_w, screen_h*0.05))
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h-screen_h*0.05, screen_w, screen_h*0.05))

            color = (100,100,100)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h*0.05, screen_w, screen_h*0.005))

            color = (240, 240, 240)
            pygame.draw.rect(self.screen, color, pygame.Rect(0, screen_h-screen_h*0.055+1, screen_w, screen_h*0.005))

        for i in self.buttons[self.s_man.get_state()]:
            if i[5]:
                rect = i[4].get_rect(topleft=(i[0], i[1]))
                self.screen.blit(i[4],rect)
            ## TODO: run func (i[5]) when clicked (do this in eventhandler)

        for i in self.elements[self.s_man.get_state()]:
            if i.get_shown():
                i.draw()

    def check_button_pressed(self, pos):
        for b in self.buttons[self.s_man.get_state()]:
            if pos[0] >= b[0] and pos[0] <= b[0]+b[2]:
                if pos[1] >= b[1] and pos[1] <= b[1]+b[3]:
                    b[len(b)-2](b[len(b)-1])
        for e in self.elements[self.s_man.get_state()]:
            for b in e.buttons:
                if pos[0] >= b[0] and pos[0] <= b[0]+b[2]:
                    if pos[1] >= b[1] and pos[1] <= b[1]+b[3]:
                        b[len(b)-2](b[len(b)-1])


    def draw_text_box(self, text, antialias, color, background, x, y):
        #text_box = self.font.render(text, antialias, color, background)
        text_box = self.font.render(text, antialias, color, background)
        self.screen.blit(text_box, (x,y))

class Element(object):

    def __init__(self, ui_manager, show):
        self.show = show
        self.ui_man = ui_manager
        self.screen = self.ui_man.screen
        self.scl = self.ui_man.scl
        self.s_man = self.ui_man.s_man
        self.init_buttons()

    def init_buttons(self):
        self.buttons = []

        self.buttons.append((0, int(self.screen.get_height()*0.055)+3*64*self.scl, 64*self.scl, 64*self.scl,
                            self.ui_man.img_energy_upgrade_icon, True, self.ui_man.run_body_relative_func, [self.ui_man.s_man, 'set_energy_level', 1]))

    def get_shown(self):
        return self.show

    def set_shown(self, value):
        self.show = value

    def draw(self):
        for i in self.buttons:
            if i[5]:
                rect = i[4].get_rect(topleft=(i[0], i[1]))
                self.screen.blit(i[4],rect)
