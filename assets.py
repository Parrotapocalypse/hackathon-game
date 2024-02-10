import pygame
def load_image(name, rotation=0, scale=1):
    surface = pygame.image.load(name)
    surface = surface.convert_alpha()

    surface = pygame.transform.rotate(surface, rotation)
    
    size = surface.get_size()
    size = (size[0] * scale, size[1] * scale)
    surface = pygame.transform.scale(surface, size)

    surface = surface.convert()
    return surface, surface.get_rect()