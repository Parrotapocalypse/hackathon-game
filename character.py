from typing import Any
import pygame as pg
import assets
MAX_TIMER = 60
class Angel(pg.sprite.Sprite):
    def __init__(self, screen) -> None:
        super().__init__()
        self.timer = MAX_TIMER
        self.image, self.rect = assets.load_image('images/angel_white.png', scale=0.25)
        colorkey = self.image.get_at((0,0))
        self.image.set_colorkey(colorkey)
        self.rect.centery = screen.get_rect().centery