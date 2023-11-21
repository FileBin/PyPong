from operator import sub
import pygame as pg
from gameobject import GameObject
from math import *
from config import PLAYER_TAG
from utils import vec2, sdbox

class Player(GameObject):
    def __init__(self, scene) -> None:
        super().__init__(scene)
        self.scale = [3, 0.4]
        self.position = [0, -6]
        self.speed = 12
        self.tag = PLAYER_TAG
        self.enable_collision = True

    def update(self, dt: float) -> None:
        inputsystem = self.scene.engine.inputsystem
        self.position[0] += inputsystem.horizontal * dt * self.speed
        limit = 10 - self.scale[0]*0.5
        self.position[0] = min(limit, max(-limit, self.position[0]))
        self.position[1] = -6

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.rect(surface=surface, color=pg.Color('#2f2fff'), rect=rect)

    def sdf(self, point: vec2) -> float:
        return sdbox(vec2(map(sub, point, self.position)), self.scale)
