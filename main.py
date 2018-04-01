import pygame
import os
import util
import resource
import cloud
import univ

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

    state_manager = util.GameStateManager(3, system, sun)
    drawer = util.Drawer(state_manager, galaxy, screen)
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

        pygame.display.flip()

main()

pygame.quit()
