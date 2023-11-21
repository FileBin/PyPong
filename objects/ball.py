import pygame as pg
from gameobject import GameObject

class Ball(GameObject):
    def __init__(self, scene) -> None:
        super().__init__(scene)
        self.speed = 2
        self.velocity = [0,0]

    def update(self, dt: float) -> None:
        pass