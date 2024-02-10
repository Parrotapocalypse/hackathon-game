from typing import Any
import pygame as pg
import assets

class Obstacle(pg.sprite.Sprite):
    def __init__(self, flipped=False) -> None:
        super().__init__()
        rotation = 0
        if flipped: rotation = 180
        self.image, self.rect = assets.load_image('images/fire.png', rotation)
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect = self.rect.move(-1,0)
