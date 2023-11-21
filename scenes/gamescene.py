from objects.obstacle import Obstacle
from scene import Scene
from objects.player import Player
from objects.world_borders import WorldBorders
from objects.ball import Ball

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
        y = 9.8
        while y > 0:
            x = -8.75
            while x < 9:
                self.objects.append(Obstacle(scene = self, position=[x,y]))
                x += 0.5
            y -= 0.45