import pygame as pg
import random as r
from gameobject import GameObject
from utils import *

class Obstacle(GameObject):
    def __init__(self, scene, position) -> None:
        super().__init__(scene)
        self.scale =  [0.5, 0.4]
        self.position = position
        self.color = [r.randint(0, 150), r.randint(0, 150), r.randint(0, 150)]

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.rect(surface=surface, color=pg.Color(self.color), rect=rect)