import pygame as pg

def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1280, 480), pg.FULLSCREEN)
    pg.display.set_caption("Biblically Accurate Angel Simulator")
    pg.mouse.set_visible(True)
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))
    screen.blit(background, (0, 0))
    rgb = [0,0,0]
    going = True
    while going:
        clock.tick(60)
        rgb = updateRGB(rgb)
        background.fill((rgb[0],rgb[1],rgb[2]))
        screen.blit(background, (0, 0))
        pg.display.flip()

def updateRGB(rgb):
    newrgb = rgb[:]
    for i,color in enumerate(rgb):
        if color == 255: newrgb[i] = 0
        else: newrgb[i] = color + 1
        if newrgb[i] != 0: break
    return newrgb
    

if __name__ == '__main__':
    main()