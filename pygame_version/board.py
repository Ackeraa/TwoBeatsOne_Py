import pygame as pg
from os import path
from settings import *

class Board:
    def __init__(self, own, opp):
        #black 1, white 0 others -1
        self.selected = [-1, -1] #piece that selected
        self.moveTo = [-1, -1] #where to move 
        self.own = own
        self.opp = opp

        self.board = [[-1 for _ in range(LINES)] for _ in range(LINES)]
        for i in range(LINES):
            self.board[i][LINES - 1] = own 
            self.board[i][0] = opp 

    def own_move(self, game):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if click[0] == 1:
            #select which piece to move
            if self.selected[0] == -1:
                selected = self.select(mouse)
                if self.board[selected[0]][selected[1]] == self.own:
                    self.selected = selected
                    print('select ', self.selected)
            else:
                #select where to move
                moveTo = self.select(mouse)
                if self.board[moveTo[0]][moveTo[1]] == self.own:
                    #select again
                    self.selected = moveTo 
                    print('select ', self.selected)
                elif self.board[moveTo[0]][moveTo[1]] == -1:
                    #move after checking valid
                    if abs(moveTo[0] - self.selected[0]) + abs(moveTo[1] - self.selected[1]) == 1:
                        self.moveTo = moveTo
            
            if self.moveTo[0] != -1:
                #move
                print('moveto ', self.moveTo)
                self.board[self.selected[0]][self.selected[1]] = -1
                self.board[self.moveTo[0]][self.moveTo[1]] = self.own 
                isWin = self.isWin(self.own, self.moveTo[0], self.moveTo[1])
                game.network.send(self.selected, self.moveTo)
                #clear
                self.selected = [-1, -1]
                self.moveTo = [-1, -1]
                game.moved = 1

    def opp_move(self, game):
        sentence = game.network.receive()
        print("received: ", sentence)
        source = [int(sentence[0]), LINES - int(sentence[2]) - 1] #mirror
        dest = [int(sentence[4]), LINES - int(sentence[6]) - 1]
        self.board[source[0]][source[1]] = -1
        self.board[dest[0]][dest[1]] = self.opp 
        isWin = self.isWin(self.opp, dest[0], dest[1])
        #oppsite moved
        game.moved = 0


    def draw(self, game):
        #plot four borders
        rect_lines = [
            ((MARGIN_LEFT, MARGIN_TOP), (WIDTH - MARGIN_LEFT, MARGIN_TOP)),
            ((MARGIN_LEFT, HEIGHT - MARGIN_TOP), (WIDTH - MARGIN_LEFT, HEIGHT - MARGIN_TOP)),
            ((MARGIN_LEFT, MARGIN_TOP), (MARGIN_LEFT, HEIGHT - MARGIN_TOP)),
            ((WIDTH - MARGIN_LEFT, MARGIN_TOP), (WIDTH - MARGIN_LEFT, HEIGHT - MARGIN_TOP))
        ]

        for line in rect_lines:
            pg.draw.line(game.screen, BLACK, line[0], line[1], 3)

        #plot inside lines
        for i in range(LINES - 2):
            pg.draw.line(game.screen, BLACK, (MARGIN_LEFT, MARGIN_TOP + (i + 1) * GRID_HEIGHT), 
                                             (WIDTH - MARGIN_LEFT, MARGIN_TOP + (i + 1) * GRID_HEIGHT), 2)

            pg.draw.line(game.screen, BLACK, (MARGIN_LEFT + (i + 1) * GRID_WIDTH, MARGIN_TOP), 
                                             (MARGIN_LEFT + (i + 1) * GRID_WIDTH, HEIGHT - MARGIN_TOP), 2)

        #plot pieces
        for i in range(LINES):
            for j in range(LINES):
                if self.board[i][j] == 0:
                    pg.draw.circle(game.screen, WHITE, self.i2c(i, j), PIECE_SIZE, PIECE_SIZE)
                elif self.board[i][j] == 1:
                    pg.draw.circle(game.screen, BLACK, self.i2c(i, j), PIECE_SIZE, PIECE_SIZE)

    
    def eat(self, x, y):
        self.board[x][y] = -1

    def isWin(self, own, x, y):
        #own: current player
        #opp: opposite player
        opp = own ^ 1

        if self.board[x][0] == opp and self.board[x][1] == own and self.board[x][2] == own and self.board[x][3] == -1:
            self.eat(x, 0)
        if self.board[x][1] == opp and self.board[x][0] == -1 and self.board[x][2] == own and self.board[x][3] == own:
            self.eat(x, 1)
        if self.board[x][2] == opp and self.board[x][3] == -1 and self.board[x][0] == own and self.board[x][1] == own:
            self.eat(x, 2)
        if self.board[x][3] == opp and self.board[x][1] == own and self.board[x][2] == own and self.board[x][0] == -1:
            self.eat(x, 3)

        if self.board[0][y] == opp and self.board[1][y] == own and self.board[2][y] == own and self.board[3][y] == -1:
            self.eat(0, y)
        if self.board[1][y] == opp and self.board[0][y] == -1 and self.board[2][y] == own and self.board[3][y] == own:
            self.eat(1, y)
        if self.board[2][y] == opp and self.board[3][y] == -1 and self.board[0][y] == own and self.board[1][y] == own:
            self.eat(2, y)
        if self.board[3][y] == opp and self.board[1][y] == own and self.board[2][y] == own and self.board[0][y] == -1:
            self.eat(3, y)

        piece_cnt = 0
        for i in range(LINES):
            for j in range(LINES):
                if self.board[i][j] == opp:
                    piece_cnt += 1
        return piece_cnt < 2

    def select(self, coor):
        index = self.c2i(coor[0], coor[1])
        coor_std = self.i2c(index[0], index[1])
        #check if valid
        if coor_std[0] >= MARGIN_LEFT and coor_std[0] <= WIDTH and coor_std[1] >= MARGIN_TOP and coor_std[1] <= HEIGHT\
                and abs(coor_std[0] - coor[0]) <= PIECE_SIZE and abs(coor_std[1] - coor[1]) <= PIECE_SIZE:
            return index 
        else:
            return [-1, -1]

    #index to coordinate
    def i2c(self, i, j):
        return [int(MARGIN_LEFT + i * GRID_WIDTH), int(MARGIN_TOP + j * GRID_HEIGHT)]

    #coordinate to index
    def c2i(self, x, y):
        return [int((x - MARGIN_LEFT + GRID_WIDTH / 2) // GRID_WIDTH), int((y - MARGIN_TOP + GRID_HEIGHT / 2) // GRID_HEIGHT)]



