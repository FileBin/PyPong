import pygame as pg
from gameobject import GameObject
from math import *

class Player(GameObject):
    def __init__(self, scene) -> None:
        super().__init__(scene)
        self.scale = [3, 0.4]
        self.position = [0, -6]
        self.speed = 7

    def update(self, dt: float) -> None:
        inputsystem = self.scene.engine.inputsystem
        self.position[0] += inputsystem.horizontal * dt * self.speed
        limit = 10 - self.scale[0]*0.5
        self.position[0] = min(limit, max(-limit, self.position[0]))

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.rect(surface=surface, color=pg.Color('#2f2fff'), rect=rect)
