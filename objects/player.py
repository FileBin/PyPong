from operator import sub
import pygame as pg
from gameobject import GameObject
from math import *
from config import PLAYER_TAG
from utils import vec2, sdbox

class Player(GameObject):
    def __init__(self, scene, borders: GameObject) -> None:
        super().__init__(scene)
        self.scale = [3, 0.4]
        self.position = [0, -9]
        self.speed = 12
        self.tag = PLAYER_TAG
        self.enable_collision = True
        self.borders = borders

    def update(self, dt: float) -> None:
        inputsystem = self.scene.engine.inputsystem
        self.position[0] += inputsystem.horizontal * dt * self.speed
        limit = self.borders.scale[0]*0.5 - self.scale[0]*0.5
        self.position[0] = min(limit, max(-limit, self.position[0]))

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.rect(surface=surface, color=pg.Color('#2f2fff'), rect=rect)

    def sdf(self, point: vec2) -> float:
        return sdbox(vec2(map(sub, point, self.position)), self.scale)
