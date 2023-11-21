from objects.obstacle import Obstacle
from scene import Scene
from objects.player import Player
from gameobject import GameObject
from objects.world_borders import WorldBorders
from objects.ball import Ball
from utils import*

class GameScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.unit_scale = 12

    def reset(self, engine) -> None:
        super().reset(engine)
        
        wb = WorldBorders(scene=self)
        player = Player(scene=self, borders=wb)

        self.objects = [
            player,
            wb,
            Ball(scene=self, player=player),
        ]
        self.objects += self.obstacle_generator(world_borders_scale=wb.scale)

    def obstacle_generator(self, world_borders_scale: vec2) -> list[GameObject]:
        obstacles = []
        gap = 0.5
        border_gap = 2
        scale_x = 3
        scale_y = 0.8
        y = 0
        while y < (world_borders_scale[1] - scale_y)/2 - border_gap:
            x = (scale_x + gap) / 2
            while x < (world_borders_scale[0] - scale_x) / 2 - border_gap:
                obstacles.append(Obstacle(scene = self, scale=[scale_x, scale_y],  position=[x,y]))
                obstacles.append(Obstacle(scene = self, scale=[scale_x, scale_y],  position=[-x,y]))
                x += scale_x + gap
            y += scale_y + gap
        return obstacles

