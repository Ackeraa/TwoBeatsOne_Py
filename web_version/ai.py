from __future__ import print_function
from settings import *
from alphaBeta import AlphaBeta


class Acker(object):
    def __init__(self, color):
        self.color = color
        self.alphaBeta = AlphaBeta(self.color, 6)

    def move(self, source, dest):
        print("FUCK POS", source, dest)
        return self.alphaBeta.move(source, dest)
