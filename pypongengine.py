import pygame as pg
from inputsystem import InputSystem
from config import *
from scene import Scene

class PyPongEngine:
    def __init__(self) -> None:
        self.inputsystem = InputSystem()
        self.active_scene: Scene = None
        self.scene_to_load: Scene = None

    def init(self, scene: Scene):
        self.active_scene = scene
        self.active_scene.reset(self)

    def run_sync(self) -> None:
        pg.init()

        self.screen=pg.display.set_mode(WINDOW_DEFAULT_SIZE, pg.RESIZABLE)
        pg.display.set_caption(WINDOW_CAPTION)
        
        self.clock=pg.time.Clock()
        
        done=False
        while done==False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done=True

            if self.scene_to_load:
                self.active_scene = self.scene_to_load
                self.scene_to_load = None
                self.active_scene.reset(self)

            dt = self.clock.tick(FPS)*0.001
            self.inputsystem.read_input()
            
            self.screen.fill(pg.Color(BG_COLOR))
            self.update(dt)

            pg.display.flip()
        pg.quit ()

    def update(self, dt: float):
        for o in self.active_scene.objects:
            if o.active:
                o.update(dt)

        for o in self.active_scene.objects:
            if o.active:
                if o.visible:
                    windowpos = self.active_scene.point_worldspace_to_windowspace(self.screen, o.position)
                    windowscale = self.active_scene.vector_worldspace_to_windowspace(self.screen, o.scale)
                    windowpos = tuple(x - y/2 for x, y in zip(windowpos, windowscale)) 
                    drawrect=pg.Rect(windowpos, windowscale)
                    o.draw(self.screen, drawrect)

    def change_scene(self, scene: Scene):
        self.scene_to_load = scene

