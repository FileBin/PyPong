import pygame as pg
from gameobject import GameObject
from utils import vec2

class WorldBorders(GameObject):
    def __init__(self, scene) -> None:
        super().__init__(scene)
        self.scale = [20, 20]
        self.is_wireframe = True
        self.drawcolor=pg.Color('#000000')
        self.enable_collision = True

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.rect(surface=surface, color=pg.Color([0,0,0]), rect=rect, width=2)

    def sdf(self, point: vec2) -> float:
        return super().sdf(point)
    
