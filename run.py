import pygame as pg
import obstacles

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

    #background.fill((170, 238, 187))
    #screen.blit(background, (0, 0))

    # set up sprites
    #angel = ...
    obstacle1 = obstacles.Obstacle()
    obstacle2 = obstacles.Obstacle(True)
    allsprites = pg.sprite.RenderPlain(obstacle1) # we could add more sprites to this group later

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
        allsprites.update()
        background.fill((200,100,50))

        # do the actual displaying of stuff
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()
    pg.quit()

if __name__ == '__main__':
    main()