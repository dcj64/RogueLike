'''#3rd party modules'''
import tcod as libtcodpy
import pygame
import constants


class struc_Tiles:
    def __init__(self, block_path):
        self.block_path = block_path


class obj_Actor:
    def __init__(self, x, y, name_object, sprite, creature=None):
        self.x = x #map address
        self.y = y #map address
        self.sprite = sprite

        if creature:
            self.creature = creature
            creature.owner = self

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x*constants.CELL_WIDTH, self.y*constants.CELL_HEIGHT))

    def move(self, dx, dy):
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy


class com_Creature:
    def __init__(self, name_instance, hp=10):

        self.name_instance = name_instance
        self.hp = hp

'''#class com_Item:'''


'''#class com_Container:'''


def map_create():
    new_map = [[struc_Tiles(False) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH)]

    new_map[4][5].block_path = True
    new_map[5][5].block_path = True
    new_map[6][5].block_path = True
    new_map[8][10].block_path = True
    new_map[9][10].block_path = True
    new_map[10][10].block_path = True
    new_map[10][11].block_path = True
    new_map[10][12].block_path = True
    new_map[15][15].block_path = True
    new_map[16][15].block_path = True
    new_map[17][15].block_path = True


    return new_map


def draw_game():

    global SURFACE_MAIN

    '''#TODO: clear the surface'''
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    '''#TODO draw the map'''
    draw_map(GAME_MAP)

    '''#TODO draw the character'''
    ENEMY.draw()
    PLAYER.draw()

    '''#TODO update the display'''
    pygame.display.flip()


def draw_map(map_to_draw):

    for x in range(0, constants.MAP_WIDTH):
        for y in range(0, constants.MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                '''#draw wall'''
                SURFACE_MAIN.blit(constants.S_WALL, (x*constants.CELL_WIDTH,y*constants.CELL_HEIGHT))
            else:
                SURFACE_MAIN.blit(constants.S_FLOOR, (x*constants.CELL_WIDTH,y*constants.CELL_HEIGHT))


def game_main_loop():
    '''#In this function, we loop the main game'''
    game_quit = False

    while not game_quit:

        '''#TODO get player input'''
        events_list = pygame.event.get()

        '''#TODO process input'''
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    PLAYER.move(0, -1)
                if event.key == pygame.K_DOWN:
                    PLAYER.move(0, 1)
                if event.key == pygame.K_LEFT:
                    PLAYER.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    PLAYER.move(1, 0)

        '''#TODO draw the game'''
        draw_game()

    '''#TODO quit the game'''
    pygame.quit()
    exit()


def game_initialize():
    '''#This function initializes the main window, and player'''

    global SURFACE_MAIN, GAME_MAP, PLAYER, ENEMY

    '''#initialize pygame'''
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH,
                                            constants.GAME_HEIGHT))
    GAME_MAP = map_create()

    creature_com1 = com_Creature("greg")
    PLAYER = obj_Actor(0, 0, "python", constants.S_PLAYER, creature=creature_com1)

    creature_com2 = com_Creature("jackie")
    ENEMY = obj_Actor(15, 16, "crab", constants.S_ENEMY, creature=creature_com2)


if __name__ == '__main__':
    game_initialize()
    game_main_loop()
