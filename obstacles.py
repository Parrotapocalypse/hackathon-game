from typing import Any
import pygame as pg
import assets
import random

class Obstacle(pg.sprite.Sprite):
    def __init__(self, screen:pg.surface.Surface, flipped=False) -> None:
        super().__init__()
        self.collided = False
        self.flipped = flipped
        self.fast = flipped
        rotation = 0
        if flipped: rotation = 180
        self.image, self.rect = assets.load_image('images/firewall_small.png', rotation, 0.25)
        # needed for transparency reasons
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)

        # should be on right side of screen to start
        topright = screen.get_rect().topright
        scaler = random.randrange(10,25) / 10
        self.image = pg.transform.scale(self.image, (self.rect.width/2,self.rect.height*scaler))
        self.rect = self.image.get_rect()
        if flipped:
            self.rect.topright = topright
        else:
            self.rect.bottomright = screen.get_rect().bottomright
    def update(self, *args: Any, **kwargs: Any):
        speed = kwargs.get('speed', 1)
        if self.fast: speed *= 1.5
        self.rect = self.rect.move(-speed,0)
        if self.rect.topright[0] < kwargs.get('screen').get_rect().topleft[0]: self.kill()
        
        angel_rect = kwargs.get('collide')
        if self.rect.colliderect(angel_rect):
            if self.flipped:
                self.collided = angel_rect.top < (self.rect.bottom + self.rect.centery)/2 and angel_rect.centerx >= self.rect.left
            else:
                self.collided = angel_rect.bottom > (self.rect.top + self.rect.centery)/2 and angel_rect.centerx >= self.rect.left