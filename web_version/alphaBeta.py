from gameState import *
from settings import *
import random

class AlphaBeta():
    def __init__(self, color, depth):

        self.own = color
        self.opp = color ^ 1
        self.depth = depth
        self.best = None

        self.board = [[-1 for _ in range(LINES)] for _ in range(LINES)]
        for i in range(LINES):
            self.board[0][i] = self.own
            self.board[LINES - 1][i] = self.opp

        self.pieces = [[], []]
        for i in range(LINES):
            self.pieces[self.own].append([0, i])
            self.pieces[self.opp].append([LINES - 1, i])

    def move(self, source, dest):

        # opp move.
        if source != [-1, -1]:
            self.board[source[0]][source[1]] = -1
            self.board[dest[0]][dest[1]] = self.opp
            for i in range(len(self.pieces[self.opp])):
                if self.pieces[self.opp][i] == source:
                    self.pieces[self.opp][i] = dest
            self.check_eat(self.opp, dest)

        if len(self.pieces[self.own]) <= 1:
            return [-1, -1], [-1, -1]
        # own move.
        self.alphaBeta(self.own, self.depth, -INF, INF)

        print(dest)
        source = self.pieces[self.own][self.best[0]]
        dest = [source[0] + self.best[1][0], source[1] + self.best[1][1]]
        self.board[source[0]][source[1]] = -1
        self.board[dest[0]][dest[1]] = self.own
        self.pieces[self.own][self.best[0]] = dest
        self.check_eat(self.own, dest)
        # for i in range(4):
        #     print(self.board[i])
        # print('-----------------')
        # print(self.pieces)
        return source, dest


    def is_legal(self, x, y):
        if x < 0 or x >= LINES or y < 0 or y >= LINES:
            return False
        if self.board[x][y] != -1:
            return False
        return True

    def eat(self, opp, pos):
        self.board[pos[0]][pos[1]] = -1
        for piece in self.pieces[opp]:
            if piece == pos:
                self.pieces[opp].remove(piece)
                break

    def check_eat(self, own, pos):
        #own: current player
        #opp: opposite player
        opp = own ^ 1
        x = pos[0]
        y = pos[1]
        board = self.board

        if board[x][0] == opp and board[x][1] == own and board[x][2] == own and board[x][3] == -1:
            self.eat(opp, [x, 0])
        if board[x][1] == opp and board[x][0] == -1 and board[x][2] == own and board[x][3] == own:
            self.eat(opp, [x, 1])
        if board[x][2] == opp and board[x][3] == -1 and board[x][0] == own and board[x][1] == own:
            self.eat(opp, [x, 2])
        if board[x][3] == opp and board[x][1] == own and board[x][2] == own and board[x][0] == -1:
            self.eat(opp, [x, 3])

        if board[0][y] == opp and self.board[1][y] == own and board[2][y] == own and board[3][y] == -1:
            self.eat(opp, [0, y])
        if board[1][y] == opp and board[0][y] == -1 and board[2][y] == own and board[3][y] == own:
            self.eat(opp, [1, y])
        if board[2][y] == opp and board[3][y] == -1 and board[0][y] == own and board[1][y] == own:
            self.eat(opp, [2, y])
        if board[3][y] == opp and board[1][y] == own and board[2][y] == own and board[0][y] == -1:
            self.eat(opp, [3, y])

    def alphaBeta(self, player, depth, alpha, beta):

        last_pieces = copy.deepcopy(self.pieces)
        last_board = copy.deepcopy(self.board)

        if len(self.pieces[self.own]) <= 1:
            return -1000 * depth
        if len(self.pieces[self.opp]) <= 1:
            return 1000 * depth

        if depth == 0:
            return random.randint(1, 5) * len(self.pieces[self.own]) - random.randint(1, 5) * len(self.pieces[1 - self.own])

        if player == self.own:
            for i in range(len(self.pieces[player])):
                piece = self.pieces[player][i]
                for dirs in DIR:
                    x = piece[0] + dirs[0]
                    y = piece[1] + dirs[1]
                    if self.is_legal(x, y):
                        self.pieces[player][i] = [x, y]
                        self.board[piece[0]][piece[1]] = -1
                        self.board[x][y] = player
                        self.check_eat(player, [x, y])

                        val = self.alphaBeta(player ^ 1, depth - 1, alpha, beta)

                        #undo
                        self.pieces = copy.deepcopy(last_pieces)
                        self.board = copy.deepcopy(last_board)

                        if val > alpha:
                            if depth == self.depth:
                                self.best = [i, dirs]
                            alpha = val
                        if alpha >= beta:
                            return alpha
            return alpha
        else:
            for i in range(len(self.pieces[player])):
                piece = self.pieces[player][i]
                for dirs in DIR:
                    x = piece[0] + dirs[0]
                    y = piece[1] + dirs[1]
                    if self.is_legal(x, y):
                        self.pieces[player][i] = [x, y]
                        self.board[piece[0]][piece[1]] = -1
                        self.board[x][y] = player
                        self.check_eat(player, [x, y])

                        val = self.alphaBeta(player ^ 1, depth - 1, alpha, beta)

                        #undo
                        self.pieces = copy.deepcopy(last_pieces)
                        self.board = copy.deepcopy(last_board)

                        if val < beta:
                            beta = val
                        if alpha >= beta:
                            return beta
            return beta
if __name__ == "__main__":
    alphaBeta = AlphaBeta(0, 4)
    alphaBeta.move([[3, 0], [2, 0]])
