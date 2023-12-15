from gameobject import GameObject
from utils import *
import pygame as pg

class Scene:
    def __init__(self) -> None:
        self.objects: list[GameObject] = []
        self.unit_scale = 10

    def reset(self, engine) -> None:
        from pypongengine import PyPongEngine
        self.engine: PyPongEngine = engine

    def update(self) -> None:
        pass

    def point_worldspace_to_windowspace(self, screen: pg.Surface, point: vec2) -> tuple[int, int]:
        windowsize = screen.get_size()
        min_dim = min(windowsize)
        
        aspect = [x / min_dim for x in windowsize]
        aspect[1] *= -1

        point = (x / self.unit_scale for x in point) # convert units to (-1..+1) range
        point = (x / y for x, y in zip(point, aspect)) # correct aspect ratio 
        point = ((x + 1) * 0.5 for x in point) # convert (+1..-1 range to 0..1 range)
        
        return tuple(int(x * y) for x, y in zip(point, windowsize))
    
    def vector_worldspace_to_windowspace(self, screen: pg.Surface, point: vec2) -> tuple[int, int]:
        windowsize = screen.get_size()
        min_dim = min(windowsize)
        
        aspect = [x / min_dim for x in windowsize]

        point = (x * 0.5 / self.unit_scale for x in point) # convert units to (-1..+1) range
        point = (x / y for x, y in zip(point, aspect)) # correct aspect ratio 
        return tuple(int(x * y) for x, y in zip(point, windowsize))
