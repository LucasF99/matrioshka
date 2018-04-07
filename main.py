import pygame
import os
import util
import data
import cloud
import univ
import tiles
import buildings
import random
import ui

def main():
    ## start pygame setup stuff
    width = 1920
    height = 1080
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0" # set window start pos to screen corner
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    done = False
    clock = pygame.time.Clock()
    framerate = 60

    dir = os.path.dirname(__file__)
    ## end pygame setup stuff

    ## start game setup stuff

    ## examples
    sun = univ.Star(pygame.image.load(os.path.join(dir,'res','star2.png')), 0, "testnameA")
    planets = [univ.Planet(pygame.image.load(os.path.join(dir,'res','planet.png')), i, "testname%d"%i)for i in range(5)]
    system = univ.System([sun], planets, 0)
    for i in range(5):
        system.planets[i].set_system(system)
    sun.set_system(system)
    galaxy = univ.Galaxy(system)

    tmap_list = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(0)
        tmap_list.append(row)

    tile_map = tiles.TileMap(tmap_list, 64, 32)

    world = cloud.World(tile_map)
    the_cloud = cloud.Cloud([world])

    build_manager = buildings.BuildingManager()
    sphere1 = buildings.Sphere()
    build_manager.add('spheres', sphere1)

    data_manager = data.DataManager()

    state_manager = util.GameStateManager(3, system, sun, world, the_cloud)

    ui_manager = ui.UIManager(state_manager, data_manager, screen)

    event_handler = util.EventHandler(state_manager, data_manager, ui_manager, galaxy, screen)

    random_event_manager = util.RandomEventManager(state_manager, data_manager)
    drawer = util.Drawer(state_manager, data_manager, ui_manager, galaxy, screen)
    ## end game setup stuff

    while not done:
        screen.fill((0,0,0))
        clock.tick(framerate)

        #print(clock.get_fps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_UP and state_manager.get_state()<4:
                    state_manager.add_state(1)
                if event.key == pygame.K_DOWN and state_manager.get_state()>2:
                    state_manager.add_state(-1)

        event_handler.update()
        drawer.draw()
        data_manager.update_data(build_manager)
        random_event_manager.update()

        pygame.display.flip()

main()

pygame.quit()
