from monteCarlo import *
from gameState import *
from settings import *
from alphaBeta import *

class AISearch():
    def __init__(self, own, own_pieces, opp_pieces, simulations_number, search_depth):

        self.own = own
        self.simulations_number = simulations_number
        self.search_depth = search_depth
        self.board = [[-1 for _ in range(LINES)] for _ in range(LINES)]
        self.best = None
        self.fuck = 0

        self.pieces = [[], []]
        for piece in own_pieces:
            if piece != None:
                self.next_to_move = piece.color
                pos = piece.pos
                self.pieces[piece.color].append(pos)
                self.board[pos[0]][pos[1]] = piece.color

        for piece in opp_pieces:
            if piece != None:
                pos = piece.pos
                self.pieces[piece.color].append(pos)
                self.board[pos[0]][pos[1]] = piece.color

    def search(self):
        self.fuck = 0
        self.alphaBeta(self.own, self.search_depth, -INF, INF, None, None)
        print("----------------", self.fuck)
        source = self.pieces[self.own][self.best[0]]
        dirs = self.best[1]
        dest = [source[0] + dirs[0], source[1] + dirs[1]] 
        print(f"AI Move from {source} to {dest}")
        return [source, dest]
        
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
        opp = 1 - own
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

    def alphaBeta(self, player, depth, alpha, beta, source, dest):
        
        last_pieces = copy.deepcopy(self.pieces)
        last_board = copy.deepcopy(self.board)

        if len(self.pieces[1 - self.own]) <= 1:
            return 1000 * depth
        if len(self.pieces[self.own]) <= 1:
            return -1000 * depth

        if depth == 0:
            '''
            print("####", len(self.pieces[self.own]), len(self.pieces[1 - self.own]))
            print(f"from {source}, to {dest}")
            for i in range(LINES):
                for j in range(LINES):
                    print("%3d" % self.board[j][i], end = "")
                print("")
            '''
            self.fuck += 1
            return len(self.pieces[self.own]) - 2 * len(self.pieces[1 - self.own])
            '''
            state = GameState(player, self.pieces, self.board)
            node = MonteCarloNode(state)
            monteCarlo = MonteCarloTreeSearch(node)
            best = monteCarlo.best_action(self.simulations_number)
            if best.parent.state.next_to_move == self.own:
                #print("FUCLLL ", best.q / best.n)
                return best.q / best.n
            else:
                return -best.q / best.n
            '''

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
                        
                        val = self.alphaBeta(1 - player, depth - 1, alpha, beta, piece, [x, y])

                        #undo
                        self.pieces = copy.deepcopy(last_pieces)
                        self.board = copy.deepcopy(last_board)

                        if val > alpha:
                            if depth == SEARCH_DEPTH:
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
                    
                        val = self.alphaBeta(1 - player, depth - 1, alpha, beta, piece, [x, y])

                        #undo
                        self.pieces = copy.deepcopy(last_pieces)
                        self.board = copy.deepcopy(last_board)

                        if val < beta:
                            beta = val
                        if alpha >= beta:
                            return beta
            return beta


