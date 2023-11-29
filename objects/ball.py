import pygame as pg
from gameobject import GameObject
from utils import *
from operator import sub
from config import *

class Ball(GameObject):
    def __init__(self, scene, player: GameObject) -> None:
        super().__init__(scene)
        self.speed = 16
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

            self.position = [lerp(x, y, 1 - pow(1 - 0.2, dt * 60)) for x, y in zip(self.position, target_position)]
        
        else:
            ball_radius = max(self.scale) * 0.5
            colliders = [x for x in self.scene.objects if x.active and x.enable_collision]
            step_distance = self.speed * dt
            
            def sdf_o(p: vec2):
                return min(list((c.sdf(p), c) for c in colliders), key=lambda t: t[0])
            
            def sdf(p: vec2):
                return sdf_o(p)[0]
            
            pos = self.position

            direction = normalize(self.velocity)

            collision = False

            dist, nearestObject = sdf_o(pos)
            while(dist - ball_radius < step_distance):
                if(dist > ball_radius):

                    phys_step = max(ball_radius*0.5, dist - ball_radius)
                    pos = list(map(add, pos, vec2(n*phys_step for n in direction)))
                    dist, nearestObject = sdf_o(pos)
                    step_distance -= phys_step
                else:
                    collision = True 
                    break

            if(collision): # collision happens
                self.position = pos
                normal = list(normal_sdf(sdf, self.position))

                # just for that type of game limit amount of normals to avoid bugs
                if all(abs(x) > 0.01 for x in normal):
                    normals = [list(normal), list(normal)]
                    normals[0][0] = 0
                    normals[1][1] = 0
                    normals = [normalize(x) for x in normals]
                    if dot(normals[0], direction) < dot(normals[1], direction):
                        normal = normals[0]
                    else:
                        normal = normals[1]
                elif abs(normal[0]) > abs(normal[1]):
                    normal[1] = 0
                else:
                    normal[0] = 0
                
                normal = normalize(normal)
                if(nearestObject.tag == PLAYER_TAG):
                    if(normal[1] >= 0):
                        self.calculate_velocity_from_player()
                else:
                    if nearestObject.tag == OBSTACLE_TAG:
                        nearestObject.active = False
                    elif nearestObject.tag == WORLDBORDER_TAG:
                        if(normal[1] > 0.5):
                            # ball hit bottom wall
                            from scenes.gamescene import GameScene 
                            self.scene.engine.change_scene(GameScene())
                    if dot(self.velocity, normal) < 0:
                        self.velocity = list(reflect(self.velocity, normal))
            self.position = [x + y * dt for x, y in zip(self.position, self.velocity)]                  

    def calculate_velocity_from_player(self):
            target_position = list(self.player.position)
            target_position[1] += 0.5

            self.velocity = list(normalize([self.position[0] - target_position[0], 1]))
            self.velocity[0] *= self.speed
            self.velocity[1] *= self.speed


    def draw(self, surface: pg.Surface, rect: pg.Rect):
        pg.draw.ellipse(surface=surface, color=pg.Color('#ff2a2a'), rect=rect)
