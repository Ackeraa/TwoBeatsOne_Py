from monteCarlo import *

class AISearch():
    def __init__(self, state, simulations_number):
        self.state = state
        self.simulations_number = simulations_number

    def search(self):
        node = MonteCarloNode(state)
        monteCarlo = MonteCarloTreeSearch(node)

        best = monteCarlo.best_action(self.simulations_number)

        return findAction(node.pieces[node.state.next_to_move], best.pieces[node.state.next_to_move])

    def findAction(parent, child):
        for i in range(len(parent)):
            if parent[i] != child[i]:
                return [parent[i], child[i]]
        
