import pygame

pygame.init()

'''#Game sizes'''
GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

'''#map vars'''
MAP_WIDTH = 30
MAP_HEIGHT = 30

'''#Color definations'''
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_RED = (204, 0, 0)

'''#Game colors'''
COLOR_DEFAULT_BG = COLOR_GREY


'''#SPRITES'''
S_PLAYER = pygame.image.load(r"C:\Users\David\Documents\GitHub\RogueLike\images\Player.png")
S_ENEMY = pygame.image.load(r"C:\Users\David\Documents\GitHub\RogueLike\images\Crab.png")
S_WALL = pygame.image.load(r"C:\Users\David\Documents\GitHub\RogueLike\images\Wall.png")
S_FLOOR = pygame.image.load(r"C:\Users\David\Documents\GitHub\RogueLike\images\Floor.jpg")
