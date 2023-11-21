#!/usr/bin/env python3
import pygame as pg, math
from config import *
from scene import Scene
from player import Player
from pypongengine import PyPongEngine

class ExampleScene(Scene):
    def reset(self, engine) -> None:
        super().reset(engine)
        self.objects = [
            Player(scene=self)
        ]

if __name__=="__main__":
    engine = PyPongEngine()
    engine.init(ExampleScene())
    engine.run_sync()