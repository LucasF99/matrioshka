import pygame
import os
import util
import data
import cloud
import univ
import tiles
import buildings

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
    sun = univ.Star(pygame.image.load(os.path.join(dir,'res','star2.png')), 0)
    system = univ.System([sun], [], 0)
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

    state_manager = util.GameStateManager(3, system, sun, world)
    drawer = util.Drawer(state_manager, data_manager, galaxy, screen)
    ## end game setup stuff

    while not done:
        screen.fill((0,0,0))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        drawer.draw()
        data_manager.update_data(build_manager)

        pygame.display.flip()

main()

pygame.quit()
