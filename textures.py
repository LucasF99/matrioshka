import pygame
import os

dir = os.path.dirname(__file__)

img = []

img.append(pygame.image.load(os.path.join(dir, "res", "sphere-placeholder.png"))) # 0 - sphere placeholder
img.append(pygame.image.load(os.path.join(dir, "res", "sphere_upgrade.png"))) # 1 - sphere upgrade
img.append(pygame.image.load(os.path.join(dir, "res", "test_red.png"))) # 2 - test red circle
