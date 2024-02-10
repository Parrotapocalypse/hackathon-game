from typing import Any
import pygame as pg
import assets

class Obstacle(pg.sprite.Sprite):
    def __init__(self, flipped=False) -> None:
        super().__init__()
        rotation = 0
        if flipped: rotation = 180
        self.image, self.rect = assets.load_image('images/fire.png', rotation)
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
    def update(self, *args: Any, **kwargs: Any):
        speed = kwargs.get('speed', 1)
        self.rect = self.rect.move(-speed,0)
        if self.rect.topright[0] < kwargs.get('screen').get_rect().topleft[0]: self.kill()