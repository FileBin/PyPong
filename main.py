#!/usr/bin/env python3
import pygame as pg, math
from pypongengine import PyPongEngine

from scenes.gamescene import GameScene

if __name__=="__main__":
    engine = PyPongEngine()
    engine.init(GameScene())
    engine.run_sync()