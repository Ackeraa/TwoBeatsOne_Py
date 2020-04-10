from settings import *
from piece import *

class Board:
    def __init__(self):
        self.ownPieces = [-1 for _ in range(LINES)]
        self.oppPieces = [-1 for _ in range(LINES)]
        self.selected = -1
        self.moved = -1

    def setPiece(self, parent, color):
        #0: white; 1: black
        self.own = color
        self.opp = color ^ 1
        #black first
        self.moved = color ^ 1 
        self.board = [[-1 for _ in range(LINES)] for _ in range(LINES)]
        for i in range(LINES):
            self.ownPieces[i] = Piece(parent, self, self.own, [i, LINES - 1])
            self.oppPieces[i] = Piece(parent, self, self.opp, [i, 0])
            self.board[i][LINES - 1] = self.own
            self.board[i][0] = self.opp

    def ownMove(self, pos):
        #is own round
        if self.moved == 1:
            return -1
        #is selected a piece
        if self.selected == -1:
            return -1

        pos = validPos(pos) 
        print("Try to MOVE: ", pos)

        #is valid move
        if pos[0] == -1 or abs(pos[0] - self.selected.pos[0]) + abs(pos[1] - self.selected.pos[1]) > 1:
            return -1
        #prereserve source and destination
        source = self.selected.pos
        dest = pos

        self.selected.move(dest)
        self.board[source[0]][source[1]] = -1
        self.board[dest[0]][dest[1]] = self.own 
        self.moved = 1
        isWin = self.isWin(self.own, dest)
        data = None
        if isWin:
            data = {'type': 'result', 'data': 'win'}
        else:
            data = {'type': 'move', 'source': [source[0], LINES - 1 - source[1]], 'dest': [dest[0], LINES - 1 - dest[1]]}

        self.selected = -1
        return data

    def oppMove(self, source, dest):
        
        print('opp moved: ', source, '->', dest)
        isWin = -1
        for piece in self.oppPieces:
            if piece != None and piece.pos == source:
                piece.move(dest)
                break

        print('check', source)
        self.printBoard('Before opp move')
        self.board[source[0]][source[1]] = -1
        self.board[dest[0]][dest[1]] = self.opp
        self.moved = 0
        isWin = self.isWin(self.opp, dest)
        self.printBoard('after opp move')

        return isWin

    def eat(self, pos):
        self.board[pos[0]][pos[1]] = -1
        print("Eat ", pos)
        for i in range(LINES):
            piece = self.ownPieces[i]
            if piece != None and piece.pos == pos:
                piece.deleteLater()
                self.ownPieces[i] = None
                break
    
        for i in range(LINES):
            piece = self.oppPieces[i]
            if piece != None and piece.pos == pos:
                piece.deleteLater()
                self.oppPieces[i] = None
                break
        for piece in self.oppPieces:
            if piece != None:
                print('oppPiece', piece)

    def printBoard(self, name):
        print(name)
        for i in range(4):
            s = ''
            for j in range(4):
                s += str(self.board[j][i]) + '  '
            print(s)


    def isWin(self, own, pos):
        #own: current player
        #opp: opposite player
        opp = own ^ 1
        x = pos[0]
        y = pos[1]
        self.printBoard('In isWin')

        if self.board[x][0] == opp and self.board[x][1] == own and self.board[x][2] == own and self.board[x][3] == -1:
            self.eat([x, 0])
            print('1')
        if self.board[x][1] == opp and self.board[x][0] == -1 and self.board[x][2] == own and self.board[x][3] == own:
            self.eat([x, 1])
            print('2')
        if self.board[x][2] == opp and self.board[x][3] == -1 and self.board[x][0] == own and self.board[x][1] == own:
            self.eat([x, 2])
            print('3')
        if self.board[x][3] == opp and self.board[x][1] == own and self.board[x][2] == own and self.board[x][0] == -1:
            self.eat([x, 3])
            print('4')

        if self.board[0][y] == opp and self.board[1][y] == own and self.board[2][y] == own and self.board[3][y] == -1:
            self.eat([0, y])
            print('5')
        if self.board[1][y] == opp and self.board[0][y] == -1 and self.board[2][y] == own and self.board[3][y] == own:
            self.eat([1, y])
            print('6')
        if self.board[2][y] == opp and self.board[3][y] == -1 and self.board[0][y] == own and self.board[1][y] == own:
            self.eat([2, y])
            print('7')
        if self.board[3][y] == opp and self.board[1][y] == own and self.board[2][y] == own and self.board[0][y] == -1:
            self.eat([3, y])
            print('8')

        piece_cnt = 0
        for i in range(LINES):
            for j in range(LINES):
                if self.board[i][j] == opp:
                    piece_cnt += 1
        return piece_cnt < 2
