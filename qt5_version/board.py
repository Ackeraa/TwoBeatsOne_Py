from settings import *
from piece import *

class Board:
    def __init__(self):
        self.ownPieces = [-1 for _ in range(LINES)]
        self.oppPieces = [-1 for _ in range(LINES)]
        self.selected = -1
        self.moveTo = -1
        self.moved = 0

    def setPiece(self, parent, color):
        #0: white; 1: black
        self.own = color
        self.opp = color ^ 1
        self.board = [[-1 for _ in range(LINES)] for _ in range(LINES)]
        for i in range(LINES):
            self.ownPieces[i] = Piece(parent, self, self.own, [i, LINES - 1])
            self.oppPieces[i] = Piece(parent, self, self.opp, [i, 0])
            self.board[i][LINES - 1] = self.own
            self.board[i][0] = self.opp

    def ownMove(self, pos):
        #is own round
        if self.moved == -1:
            return
        #is selected a piece
        if self.selected == -1:
            return 

        pos = validPos(pos) 
        print("Try to MOVE: ", pos)

        #is valid move
        if pos[0] == -1 or abs(pos[0] - self.selected.pos[0]) + abs(pos[1] - self.selected.pos[1]) > 1:
            return
        self.selected.move(pos)
        self.board[self.selected.pos[0]][self.selected.pos[1]] = -1
        self.board[pos[0]][pos[1]] = self.own 
        self.moved = 1
        self.selected = -1
    
    def oppMove(self, source, dest):
        
        for piece in self.oppPieces:
            if piece.pos == source:
                piece.move(dest)
                break

        self.board[source[0]][source[1]] = -1
        self.board[dest[0]][dest[1]] = self.opp
        self.moved = 0

    def eat(self, pos):
        self.board[pos[0]][pos[1]] = -1
        for piece in self.ownPieces:
            if piece.pos == pos:
                piece.deleteLater()
                piece = None
                break
        for piece in self.oppPieces:
            if piece.pos == pos:
                piece.deleteLater()
                piece = None

                break

    def isWin(self, own, pos):
        #own: current player
        #opp: opposite player
        opp = own ^ 1
        x = pos[0]
        y = pos[1]

        if self.board[x][0] == opp and self.board[x][1] == own and self.board[x][2] == own and self.board[x][3] == -1:
            self.eat([x, 0])
        if self.board[x][1] == opp and self.board[x][0] == -1 and self.board[x][2] == own and self.board[x][3] == own:
            self.eat([x, 1])
        if self.board[x][2] == opp and self.board[x][3] == -1 and self.board[x][0] == own and self.board[x][1] == own:
            self.eat([x, 2])
        if self.board[x][3] == opp and self.board[x][1] == own and self.board[x][2] == own and self.board[x][0] == -1:
            self.eat([x, 3])

        if self.board[0][y] == opp and self.board[1][y] == own and self.board[2][y] == own and self.board[3][y] == -1:
            self.eat([x, y])
        if self.board[1][y] == opp and self.board[0][y] == -1 and self.board[2][y] == own and self.board[3][y] == own:
            self.eat([x, 1])
        if self.board[2][y] == opp and self.board[3][y] == -1 and self.board[0][y] == own and self.board[1][y] == own:
            self.eat([x, 2])
        if self.board[3][y] == opp and self.board[1][y] == own and self.board[2][y] == own and self.board[0][y] == -1:
            self.eat([x, 3])

        piece_cnt = 0
        for i in range(LINES):
            for j in range(LINES):
                if self.board[i][j] == opp:
                    piece_cnt += 1
        return piece_cnt < 2
