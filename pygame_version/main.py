import pygame as pg
import random
from settings import *
from board import *
from network import *
from os import path

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.network = Network(self)
        self.board = Board(self.color, self.color ^ 1) 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.moved = self.color ^ 1 #black first
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        #white player show board directly
        if self.color == 0:
            self.draw()



    def load_data(self):
        self.dir = path.dirname(__file__)
        self.img_dir = path.join(self.dir, 'img')
        self.bgi = pg.image.load(path.join(self.img_dir, 'bgi.png'))
        self.bgi = pg.transform.scale(self.bgi, (WIDTH, HEIGHT))
    
    def new(self):
        self.run()

    def run(self):
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        if self.moved == 0:
            self.board.own_move(self)
        else:
            self.board.opp_move(self)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.blit((self.bgi), (0, 0))
        self.board.draw(self)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_end_screen(self):
        pass

    def wait_for_key(self):
        pass

    def draw_text(self, text, size, color, x, y):
        pass

if __name__ == "__main__":
    g = Game()
    g.show_start_screen()
    g.new()
   # while g.running:
     #   g.new()
    #    g.show_end_screen()

    pg.quit()
    
