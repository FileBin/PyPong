#!/usr/bin/env python3
import pygame as pg, math
from utils import *
from config import *
from scene import Scene
from pypongengine import PyPongEngine

from objects.world_borders import WorldBorders
from objects.player import Player
from objects.obstacle import Obstacle

class ExampleScene(Scene):
    def reset(self, engine) -> None:
        super().reset(engine)
        self.objects = [
            Player(scene=self),
            WorldBorders(scene=self)
        ]
        y = 9.8
        while y > 0:
            x = -8.75
            while x < 9:
                self.objects.append(Obstacle(scene = self, position=[x,y]))
                x += 0.5
            y -= 0.45

if __name__=="__main__":
    engine = PyPongEngine()
    engine.init(ExampleScene())
    engine.run_sync()