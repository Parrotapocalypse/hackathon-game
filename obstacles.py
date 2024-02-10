from typing import Any
import pygame as pg
import assets
import random

class Obstacle(pg.sprite.Sprite):
    def __init__(self, screen:pg.surface.Surface, flipped=False) -> None:
        super().__init__()
        rotation = 0
        if flipped: rotation = 180
        self.image, self.rect = assets.load_image('images/fire.png', rotation)
        # needed for transparency reasons
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)

        # should be on right side of screen to start
        topright = screen.get_rect().topright
        self.rect.centerx = topright[0]
        if flipped:
            self.rect.centery = topright[1] + random.randrange(0,screen.get_rect().centery)
        else:
            self.rect.centery = screen.get_rect().bottomright[1] + random.randrange(0,screen.get_rect().centery)
    def update(self, *args: Any, **kwargs: Any):
        speed = kwargs.get('speed', 1)
        self.rect = self.rect.move(-speed,0)
        if self.rect.topright[0] < kwargs.get('screen').get_rect().topleft[0]: self.kill()