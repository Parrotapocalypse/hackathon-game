import pygame as pg
import obstacles
import random
import character
import math

# constants
MAX_OBSTACLES = 3
SPEED = 2
SQRT = math.sqrt(SPEED)
ACCELERATION = 1.5e-3

def main():
    # set up main game stuff
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
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
    obstacle3 = obstacles.Obstacle(screen, rand_bool())
    allsprites = pg.sprite.RenderPlain((angel, obstacle1, obstacle2, obstacle3))
    spriteobstacles = pg.sprite.RenderPlain((obstacle1, obstacle2, obstacle3))
    going = True # infinite game loop
    howfast = 0
    score = 0
    while going:
        clock.tick(60)
        # check for interaction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    going = False
        pressed = pg.key.get_pressed()
        def delta(x,y):
            angel.rect.x += x
            angel.rect.y += y
        if pressed[pg.K_UP]:
            if pressed[pg.K_LEFT]: delta(-SQRT,-SQRT)
            elif pressed[pg.K_RIGHT]: delta(SQRT,-SQRT)
            else: angel.rect.y -= SPEED
        elif pressed[pg.K_DOWN]:
            if pressed[pg.K_LEFT]: delta(-SQRT,SQRT)
            elif pressed[pg.K_RIGHT]: delta(SQRT,SQRT)
            else: angel.rect.y += SPEED
        elif pressed[pg.K_LEFT]: angel.rect.x -= SPEED
        elif pressed[pg.K_RIGHT]: angel.rect.x += SPEED
        allsprites.update(speed=1+howfast, screen=screen, collide=angel.rect)
        for obst in spriteobstacles:
            if obst.collided: going = False
        # sprites might have been removed from the group
        if len(spriteobstacles) < MAX_OBSTACLES:
            score += 1
            sprite = obstacles.Obstacle(screen, rand_bool())
            allsprites.add(sprite)
            spriteobstacles.add(sprite)
            if sprite.flipped: sprite.rect.topright = screen.get_rect().topright
            else: sprite.rect.bottomright = screen.get_rect().bottomright
        image.fill((200,100,50))
        # do the actual displaying of stuff
        allsprites.draw(image)
        background.blit(image, (0,0))
        screen.blit(background, (0,0))
        pg.display.flip()
        howfast += ACCELERATION
    font = pg.font.Font(None, 64)
    text = font.render(f"Your Score: {score}. Press any key to exit", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)
    screen.blit(background, (0,0))
    pg.display.flip()
    e = pg.event.wait()
    while e.type != pg.KEYDOWN: e = pg.event.wait()
    pg.quit()

def rand_bool():
    return random.randint(0,1) == 0

if __name__ == '__main__':
    main()