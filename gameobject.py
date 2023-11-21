import pygame as pg
from utils import *

class GameObject:
    def __init__(self, scene) -> None:
        self.active = True
        self.visible = True
        self.enable_collision = False
        self.position: vec2 = [0, 0]
        self.scale: vec2 = [1, 1]
        self.drawcolor = pg.Color([0,0,0])
        self.is_wireframe = False
        from scene import Scene
        self.scene : Scene = scene

    def update(self, dt: float) -> None:
        pass

    def sdf(self, point: vec2) -> float:
        pass