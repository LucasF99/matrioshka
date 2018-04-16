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

    def set_done(value):
        done = value
    ## end pygame setup stuff

    ## start game setup stuff

    ## examples
    sun = univ.Star(pygame.image.load(os.path.join(dir,'res','star2.png')), 0, " testnameA ")
    planets = [univ.Planet(pygame.image.load(os.path.join(dir,'res','planet.png')), i, " testname%d "%i)for i in range(5)]
    system = univ.System([sun], planets, 0)
    for i in range(5):
        system.planets[i].set_system(system)
    sun.set_system(system)
    galaxy = univ.Galaxy(system)

    tmap_list = []
    for i in range(50):
        row = []
        for j in range(50):
            row.append(0)
        tmap_list.append(row)

    tile_map = tiles.TileMap(tmap_list, 64, 64)

    world = cloud.World(tile_map)
    the_cloud = cloud.Cloud([world])

    build_manager = buildings.BuildingManager()
    sphere1 = buildings.Sphere()
    build_manager.add('spheres', sphere1)

    data_manager = data.DataManager()

    state_manager = util.GameStateManager(3, system, sun, world, the_cloud)

    ui_manager = ui.UIManager(state_manager, data_manager, screen)

    drawer = util.Drawer(state_manager, data_manager, ui_manager, galaxy, screen)

    event_handler = util.EventHandler(state_manager, data_manager, ui_manager, build_manager, drawer, galaxy, screen)

    random_event_manager = util.RandomEventManager(state_manager, data_manager)

    ## end game setup stuff

    while not state_manager.get_done():
        screen.fill((0,0,0))
        clock.tick(framerate)

        #print(clock.get_fps())

        event_handler.update()
        drawer.draw()
        data_manager.update_data(build_manager, clock.get_time())
        random_event_manager.update()

        pygame.display.flip()

main()

pygame.quit()
