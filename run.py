import pygame as pg

def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1280, 480), pg.SCALED)
    pg.display.set_caption("Biblically Accurate Angel Simulator")
    pg.mouse.set_visible(True)
    background = pg.Surface(screen.get_size())
    background = background.convert()
    
    pg.draw.circle(background, pg.Color(100,0,100), (0,0), 5)
    screen.blit(background, (0,0))

    going = True
    while going:
        clock.tick(60)

if __name__ == '__main__':
    main()