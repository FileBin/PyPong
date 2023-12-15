import pygame as pg

WINDOW_DEFAULT_SIZE = [800,600]
WINDOW_CAPTION = "PyPong"
FPS = 60

BG_COLOR='#02ed8f'

#Input config
HORIZONTAL_AXIS_POSITIVE=[pg.K_RIGHT, pg.K_d]
HORIZONTAL_AXIS_NEGATIVE=[pg.K_LEFT, pg.K_a]
ACTION_POSITIVE=[pg.K_SPACE, pg.K_UP]

# Tags
PLAYER_TAG = 'player'
WORLDBORDER_TAG = 'worldborder'
OBSTACLE_TAG = 'obstacle'

IMMORTABLE=False
