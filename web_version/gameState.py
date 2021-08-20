import copy
from settings import *

#color: 0, 1

class GameState():
    def __init__(self, next_to_move, pieces, board):
        
        self.next_to_move = next_to_move
        self.pieces = pieces
        self.board = board
        
    @property
    def game_result(self):
        if len(self.pieces[self.next_to_move]) <= 1:
            return 1 - self.next_to_move
        else:
            return self.next_to_move

    def is_game_over(self):
        return len(self.pieces[self.next_to_move]) <= 1 or len(self.pieces[1 - self.next_to_move]) <= 1

    def move(self, action):
        sourcePiece = action[0] #source Piece i
        destPos = action[1] #destination (x, y)
        new_state = copy.deepcopy(self)
        
        source_x = self.pieces[self.next_to_move][sourcePiece][0]
        source_y = self.pieces[self.next_to_move][sourcePiece][1]

        new_state.board[source_x][source_y] = -1
        new_state.board[destPos[0]][destPos[1]] = self.next_to_move
        new_state.pieces[self.next_to_move][sourcePiece] = destPos.copy()
        self.check_eat(new_state, destPos)
        new_state.next_to_move = 1 - self.next_to_move

        return new_state

    def is_legal(self, x, y):
        if x < 0 or x >= LINES or y < 0 or y >= LINES:
            return False
        if self.board[x][y] != -1:
            return False
        return True

    def get_legal_actions(self):
        actions = []
        for i in range(len(self.pieces[self.next_to_move])):
            piece = self.pieces[self.next_to_move][i]
            #format [source_piece_id, [dest_x, dest_y]]
            if self.is_legal(piece[0] + 1, piece[1]):
                actions.append([i, [piece[0] + 1, piece[1]]])
            if self.is_legal(piece[0] - 1, piece[1]):
                actions.append([i, [piece[0] - 1, piece[1]]])
            if self.is_legal(piece[0], piece[1] + 1):
                actions.append([i, [piece[0], piece[1] + 1]])
            if self.is_legal(piece[0], piece[1] - 1):
                actions.append([i, [piece[0], piece[1] - 1]])
        #print("FUCK", actions)
        return actions

    def eat(self, state, pos):
        state.board[pos[0]][pos[1]] = -1
        for piece in state.pieces[1 - state.next_to_move]:
            if piece == pos:
                state.pieces[1 - state.next_to_move].remove(piece)
                break
    
    def check_eat(self, state, pos):
        #own: current player
        #opp: opposite player
        own = state.next_to_move
        opp = 1 - own
        x = pos[0]
        y = pos[1]

        if state.board[x][0] == opp and state.board[x][1] == own and state.board[x][2] == own and state.board[x][3] == -1:
            self.eat(state, [x, 0])
        if state.board[x][1] == opp and state.board[x][0] == -1 and state.board[x][2] == own and state.board[x][3] == own:
            self.eat(state, [x, 1])
        if state.board[x][2] == opp and state.board[x][3] == -1 and state.board[x][0] == own and state.board[x][1] == own:
            self.eat(state, [x, 2])
        if state.board[x][3] == opp and state.board[x][1] == own and state.board[x][2] == own and state.board[x][0] == -1:
            self.eat(state, [x, 3])

        if state.board[0][y] == opp and self.board[1][y] == own and state.board[2][y] == own and state.board[3][y] == -1:
            self.eat(state, [0, y])
        if state.board[1][y] == opp and state.board[0][y] == -1 and state.board[2][y] == own and state.board[3][y] == own:
            self.eat(state, [1, y])
        if state.board[2][y] == opp and state.board[3][y] == -1 and state.board[0][y] == own and state.board[1][y] == own:
            self.eat(state, [2, y])
        if state.board[3][y] == opp and state.board[1][y] == own and state.board[2][y] == own and state.board[0][y] == -1:
            self.eat(state, [3, y])

