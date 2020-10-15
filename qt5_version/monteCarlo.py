import numpy as np
from collections import defaultdict
from game_state import *

class MonteCarloNode():
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent
        self.children = []
        self._number_of_visits = 0.
        self._results = defaultdict(int)
        self._untried_actions = None

    @property
    def untried_actions(self):
        if self._untried_actions is None:
            self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions 

    @property
    def q(self):
        wins = self._results[self.parent.state.next_to_move]
        loses = self._results[-1 * self.parent.state.next_to_move]
        return wins - loses

    @property
    def n(self):
        return self._number_of_visits

    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MonteCarloNode(next_state, parent = self)
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        return self.state.is_game_over()

    def rollout(self):
        current_rollout_state = self.state
        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result

    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1. 
        if self.parent:
            self.parent.backpropagate(result)

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param = 1.4):
        choice_weight = [
                (c.q / c.n) + c_param * np.sqrt((2 * np.log(self.n) / c.n))
                for c in self.children
        ]
        return self.children[np.argmax(choice_weight)]

    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]

class MonteCarloTreeSearch(object):
    def __init__(self, node):
        self.root = node

    def best_action(self, simulations_number):

        for _ in range(0, simulations_number):
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        
        return self.root.best_child(c_param = 0.)

    def _tree_policy(self):
        current_node = self.root
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

def build_tree(node):

    print(f'parent: [{node.parent.state.board.l}, {node.parent.state.board.r}], [l, r]: [{node.state.board.l}, {node.state.board.r}], sum: {node.state.board.sum}, visits: {node._number_of_visits}, results: {node._results[1]}, {node._results[-1]}')
    if len(node.children) == 0:
        return 
    build_tree(node.children[0])
    if len(node.children) == 2:
        build_tree(node.children[1])
