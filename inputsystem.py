import pygame as pg
from config import *

class InputSystem:
    def __init__(self) -> None:
        self.horizontal = 0
        self.action = False
        self.action_pressed = False
    
    def read_input(self) -> None:
        keys = pg.key.get_pressed()

        self.horizontal = 0
        self.horizontal += 1 if any(keys[x] for x in HORIZONTAL_AXIS_POSITIVE) else 0
        self.horizontal -= 1 if any(keys[x] for x in HORIZONTAL_AXIS_NEGATIVE) else 0

        action_old_state = self.action
        self.action = any(keys[x] for x in ACTION_POSITIVE)

        self.action_pressed = self.action and not action_old_state