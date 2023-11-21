import pygame as pg
import random as r
from gameobject import GameObject
from utils import *
from config import OBSTACLE_TAG

class Obstacle(GameObject):
    def __init__(self, scene, scale, position) -> None:
        super().__init__(scene)
        self.scale =  [2, 1.5]
        self.position = position
        self.color = [r.randint(0, 150), r.randint(0, 150), r.randint(0, 150)]
        self.enable_collision = True
        self.tag = OBSTACLE_TAG

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.rect(surface=surface, color=pg.Color(self.color), rect=rect)

    def sdf(self, point: vec2) -> float:
        return sdbox(vec2(map(sub, point, self.position)), self.scale)