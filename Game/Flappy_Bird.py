import os, sys, random
import pygame as pg

FPS = 60
PIPE_ADD_INTERVAL = 3000
FRAME_BIRD_JUMP_HEIGHT = 5
FRAME_BIRD_DROP_HEIGHT = 3

size = width, height = 400, 708

log = True

running = True

def load_image(file):
    
    #Load Image easily

    pathname = os.path.dirname(sys.argv[0])       
    file = os.path.join(os.path.abspath(pathname), "Images", file)
    surface = pg.image.load(file)

def game_over():
    font = pg.font.Font(Default, 36)
    text = font.render("Game Over", 1, (255, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = background .get_rect().centerx


def main():
    pg.init()
    if log == True: 
        print("[Log] Pygame Started")

    clock = pg.time.Clock()

    game_over()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
    clock.tick(FPS)

    pg.quit()


screen = pg.display.set_mode((width, height))
pg.display.set_caption("Flappy Bird")

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


main()
