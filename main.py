#!/usr/bin/env python3
import pygame as pg, math
from config import *
from scene import Scene
from pypongengine import PyPongEngine

from objects.world_borders import WorldBorders
from objects.player import Player
from objects.ball import Ball

from scenes.gamescene import GameScene

class ExampleScene(Scene):
    def reset(self, engine) -> None:
        super().reset(engine)
        player = Player(scene=self)

        self.objects = [
            player,
            WorldBorders(scene=self),
            Ball(scene=self, player=player),
        ]

if __name__=="__main__":
    engine = PyPongEngine()
    engine.init(GameScene())
    engine.run_sync()