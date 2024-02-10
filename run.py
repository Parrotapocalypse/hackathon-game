import pygame as pg
import obstacles
import random
import character

# constants
MAX_OBSTACLES = 2
JUMP_SPEED_GAIN = -0.5

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
    angel = character.Angel(screen)
    obstacle1 = obstacles.Obstacle(screen)
    obstacle2 = obstacles.Obstacle(screen, True)
    allsprites = pg.sprite.RenderPlain((angel, obstacle1, obstacle2))
    spriteobstacles = pg.sprite.RenderPlain((obstacle1, obstacle2))
    going = True # infinite game loop
    howfast = 0
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
                    angel.velocity += JUMP_SPEED_GAIN
        allsprites.update(speed=1+howfast, screen=screen)
        # sprites might have been removed from the group
        if len(spriteobstacles) < MAX_OBSTACLES:
            sprite = obstacles.Obstacle(screen, rand_bool())
            allsprites.add(sprite)
            spriteobstacles.add(sprite)
        image.fill((200,100,50))
        # do the actual displaying of stuff
        allsprites.draw(image)
        background.blit(image, (0,0))
        screen.blit(background, (0,0))
        pg.display.flip()
        howfast += 1e-2
    pg.quit()

def rand_bool():
    return random.randint(0,1) == 0

if __name__ == '__main__':
    main()