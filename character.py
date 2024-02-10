from typing import Any
import pygame as pg
import assets

class Angel(pg.sprite.Sprite):
    def __init__(self, screen) -> None:
        super().__init__()
        self.velocity = 0
        self.image, self.rect = assets.load_image('images/angel.png', scale=0.25)
        #colorkey = self.image.get_at((0,0))
        #self.image.set_colorkey(colorkey)
        self.rect.center = screen.get_rect().center
    def update(self, *args: Any, **kwargs: Any):
        # negative y direction is up, positive is down (because top left is 0,0)
        self.rect.move_ip(self.rect.x, self.rect.y-self.velocity)
        self.velocity += 1