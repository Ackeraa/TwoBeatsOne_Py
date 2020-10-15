import copy

class GameState():
    def __init__(self, ownPiece, oppPiece):
        self.next_to_move = own.Piece.color
        self.pieces = [[], []]
        self.board = [[0 for _ in range(LINES)] for _ in range(LINES)]
        for piece in ownPiece:
            pos = piece.pos
            self.pieces[piece.color].append(pos)
            self.board[pos[0]][pos[1]] = piece.color

        for piece in oppPiece:
            pos = piece.pos
            self.pieces[piece.color].append(pos)
            self.board[pos[0]][pos[1]] = piece.color
        
    @property
    def gameResult(self):
        if len(self.ownPiece) == 0:
            return -1
        else if len(self.oppPiece) == 0:
            return 1
        else return 0

    def isGameOver(self):
        if len(self.ownPiece) + len(self.oppPiece) == 0:
            return 1
        else:
            return 0

    def move(self, action):
        sourcePiece = action[0]
        destPos = action[1]
        new_state = self.copy()
        
        source_x = self.pieces[self.next_to_move][sourcePiece][0]
        source_y = self.pieces[self.next_to_move][sourcePiece][1]

        new_state.board[source_x][source_y] = 0
        new_state.board[destPos[0]][destPos[1]] = self.next_to_move
        
        new_state.pieces[self.next_to_move][sourcePiece] = destPos.copy()

        return new_state

    def isLegal(x, y):
        if x < 0 || x >= LINES || y < 0 || y >= LINES:
            return False
        if self.board[x][y] != 0:
            return False
        return True

    def getLegalActions(self):
        actions = []
        for piece in self.pieces[self.next_to_move]:
            if isLegal(piece[0] + 1, piece[1]):
                actions.append(piece[0] + 1, piece[1])
            if isLegal(piece[0] - 1, piece[1]):
                actions.append(piece[0] - 1, piece[1])
            if isLegal(piece[0], piece[1] + 1):
                actions.append(piece[0], piece[1] + 1)
            if isLegal(piece[0], piece[1] - 1):
                actions.append(piece[0], piece[1] - 1)
        return actions



