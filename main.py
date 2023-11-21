#!/usr/bin/env python3
import pygame as pg, math
from config import *



if __name__=="__main__":
    # Used to manage how fast the screen updates
    pg.init()
    screen=pg.display.set_mode(WINDOW_DEFAULT_SIZE, pg.RESIZABLE)
    pg.display.set_caption(WINDOW_CAPTION)
    
    clock=pg.time.Clock()
    done=False

    while done==False:
        for event in pg.event.get(): # User did something
            if event.type == pg.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
        
        dt = clock.tick(FPS)
        screen.fill([0,0,0])

        # Swap draw buffers
        pg.display.flip()
    pg.quit ()