import pygame as pg
import obstacles
import random

# constants
MAX_OBSTACLES = 2

def main():
    # set up main game stuff
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1280, 480), pg.FULLSCREEN)
    pg.display.set_caption("Biblically Accurate Angel Simulator")
    pg.mouse.set_visible(True)
    # set up background and display it
    background = pg.Surface(screen.get_size())
    background = background.convert()
    image = pg.Surface(background.get_size(), pg.SRCALPHA)
    image.convert()
    
    # set up sprites
    #angel = ...
    obstacle1 = obstacles.Obstacle()
    obstacle2 = obstacles.Obstacle(True)
    allsprites = pg.sprite.RenderPlain((obstacle1, obstacle2)) # we could add more sprites to this group later
    
    going = True # infinite game loop
    while going:
        clock.tick(60)
        # check for interaction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    going = False
                elif event.key == pg.K_SPACE:
                    pass
            elif event.type == pg.MOUSEBUTTONDOWN:
                pass
        allsprites.update(speed=1, screen=screen)
        # sprites might have been removed from the group
        if len(allsprites) < MAX_OBSTACLES:
            allsprites.add(obstacles.Obstacle(rand_bool()))
        image.fill((200,100,50))
        # do the actual displaying of stuff
        allsprites.draw(image)
        background.blit(image, (0,0))
        screen.blit(background, (0, 0))
        pg.display.flip()
        
    pg.quit()

def rand_bool():
    return random.randint(0,1) == 0

if __name__ == '__main__':
    main()