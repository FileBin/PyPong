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
        scale_x = world_borders_scale[0] / 20
        scale_y = world_borders_scale[1] / 14
        y =  (0 + world_borders_scale[1]) / 2 - scale_y / 2 - 0.1
        while y > 0:
            x = (0 - world_borders_scale[0]) / 2 + scale_x / 2 + 0.1
            while x < (0 + world_borders_scale[0]) / 2:
                obstacles.append(Obstacle(scene = self, scale=[scale_x, scale_y],  position=[x,y]))
                x += scale_x + 0.2
            y -= scale_y + 0.1
        return obstacles

