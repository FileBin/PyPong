import pygame as pg
from gameobject import GameObject
from utils import *
from operator import sub
from config import *

class Ball(GameObject):
    def __init__(self, scene, player: GameObject) -> None:
        super().__init__(scene)
        self.speed = 20
        self.velocity = [0,0]
        self.launched = False
        self.player = player
        self.scale = [0.7]*2

    def update(self, dt: float) -> None:
        inputsystem = self.scene.engine.inputsystem

        if not self.launched:

            target_position = list(self.player.position)
            target_position[1] += 0.5

            if inputsystem.action_pressed:
                self.calculate_velocity_from_player()
                self.launched = True
                return

            self.position = [lerp(x, y, 0.2) for x, y in zip(self.position, target_position)]
        
        else:
            colliders = [x for x in self.scene.objects if x.active and x.enable_collision]
            def sdf_o(p: vec2):
                return min(list((c.sdf(p), c) for c in colliders), key=lambda t: t[0])
            
            def sdf(p: vec2):
                return sdf_o(p)[0]
            
            ball_radius = max(self.scale) * 0.5

            dist, nearestObject = sdf_o(self.position)
            if(dist < ball_radius): # collision happens
                #offset = ball_radius - dist
                #offset = [x * offset for x in normalize(self.velocity)]
                #self.position = list(map(sub, self.position, offset))
                normal = normal_sdf(sdf, self.position)
                if(nearestObject.tag == PLAYER_TAG):
                    if(normal[1] > 0):
                       self.calculate_velocity_from_player()
                else:
                    if nearestObject.tag == OBSTACLE_TAG:
                        nearestObject.active = False
                    elif nearestObject.tag == WORLDBORDER_TAG:
                        if(normal[1] > 0.5):
                            # ball hit bottom wall
                            from scenes.gamescene import GameScene 
                            self.scene.engine.change_scene(GameScene())

                    self.velocity = list(reflect(self.velocity, normal))             

            self.position = [x + y * dt for x, y in zip(self.position, self.velocity)]

    def calculate_velocity_from_player(self):
            target_position = list(self.player.position)
            target_position[1] += 0.5

            self.velocity = list(normalize([self.position[0] - target_position[0], 2]))
            self.velocity[0] *= self.speed
            self.velocity[1] *= self.speed


    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.ellipse(surface=surface, color=pg.Color('#ff2a2a'), rect=rect)