from operator import sub
import pygame as pg
import pygame.freetype as pgfreetype
from gameobject import GameObject
from math import *
from utils import vec2, sdbox

class Text(GameObject):
    def __init__(self, scene, text: str, position: vec2, scale: vec2, color = pg.Color('#000000')) -> None:
        super().__init__(scene)
        self.current_size = None
        self.scale = scale
        self.position = position
        self.text = text
        self.color = color

    def draw(self, surface: pg.Surface, rect: pg.Rect):
        if (self.current_size != rect.height):
            self.current_size = rect.height
            self.font = pgfreetype.Font('res/arial.ttf', rect.height)
        self.font.render_to(surf=surface, dest=rect, text=self.text, fgcolor=self.color)
