from utils.constants import GRID_SIZE
from .q_learning import QLearning

class RLAgent:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.q_learning = QLearning()

    def choose_action(self, board):
        state = self.q_learning.get_state(board.grid)
        valid_actions = self.get_valid_actions(board)
        return self.q_learning.get_action(state, valid_actions)

    def get_valid_actions(self, board):
        actions = []
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if not board.grid[row][col]:
                    actions.append((row, col))
        return actions

    def update_q_table(self, board, action, reward, next_board):
        state = self.q_learning.get_state(board.grid)
        next_state = self.q_learning.get_state(next_board.grid)
        valid_actions = self.get_valid_actions(next_board)
        self.q_learning.update(state, action, reward, next_state, valid_actions)
        
    def printTable(self):
        self.q_learning.printTable()
