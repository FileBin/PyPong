import pygame as pg
from gameobject import GameObject

class WorldBorders(GameObject):
    def __init__(self, scene) -> None:
        super().__init__(scene)
        self.scale = [20, 20]
        self.is_wireframe = True
        self.drawcolor=pg.Color('#000000')
    
