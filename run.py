import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((1280, 480), pg.SCALED)
    pg.display.set_caption("Biblically Accurate Angel Simulator")
    pg.mouse.set_visible(False)
    background = pg.Surface(screen.get_size())

    pg.draw.circle(background, pg.Color(100,0,100), (0,0), 5)
    input()

if __name__ == '__main__':
    main()