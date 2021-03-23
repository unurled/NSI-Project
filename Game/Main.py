import pygame as pg
import os

SCREENRECT = pg.Rect(0, 0, 640, 480)
main_dir = "/data/DOCUMENT/prog/school/NSI-Project/Game/"

def load_image(file):
    """ loads an image, prepares it for play
    """
    file = os.path.join(main_dir, "Images", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()

def main(winstyle=0):
    pg.init()

    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    background = load_image("background.png")

    icon = pg.transform.scale(load_image("bird1.png"), (32, 32))
    pg.display.set_icon(icon)
    pg.display.set_caption("Flappy Bird")

    bgdtile = load_image("background.png")
    background = pg.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pg.display.flip()

    clock = pg.time.Clock()

    alive = True

    while alive:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
    
    keystate = pg.key.get_pressed()

    clock.tick(60)


main()