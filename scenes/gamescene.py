from scene import Scene
from objects.player import Player
from objects.world_borders import WorldBorders
from objects.ball import Ball

class GameScene(Scene):
    def reset(self, engine) -> None:
        super().reset(engine)
        player = Player(scene=self)
        
        self.objects = [
            player,
            WorldBorders(scene=self),
            Ball(scene=self, player=player),
        ]