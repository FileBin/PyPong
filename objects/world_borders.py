import pygame as pg
from gameobject import GameObject
from utils import *
from config import WORLDBORDER_TAG

class WorldBorders(GameObject):
    def __init__(self, scene) -> None:
        super().__init__(scene)
        self.scale = [36, 20]
        self.is_wireframe = True
        self.drawcolor=pg.Color('#000000')
        self.enable_collision = True
        self.tag = WORLDBORDER_TAG

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.rect(surface=surface, color=pg.Color([0,0,0]), rect=rect, width=2)

    def sdf(self, point: vec2) -> float:
        return -sdbox(point, self.scale)
    
