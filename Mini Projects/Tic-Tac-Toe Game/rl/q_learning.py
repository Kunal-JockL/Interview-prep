#import numpy as np
import random
from utils.constants import GRID_SIZE

class QLearning:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}  # State-action values
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate

    def get_state(self, grid):
        """Convert the board into a tuple representing the state."""
        return tuple(tuple(row) for row in grid)

    def get_action(self, state, valid_actions):
        """Choose an action using epsilon-greedy policy."""
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(valid_actions)  # Explore
        else:
            return self.best_action(state, valid_actions)  # Exploit

    def best_action(self, state, valid_actions):
        """Get the action with the highest Q-value."""
        q_values = [self.q_table.get((state, action), 0) for action in valid_actions]
        max_q = max(q_values, default=0)
        best_actions = [a for a, q in zip(valid_actions, q_values) if q == max_q]
        return random.choice(best_actions) if best_actions else random.choice(valid_actions)

    def update(self, state, action, reward, next_state, valid_actions):
        """Update Q-value using the Bellman equation."""
        current_q = self.q_table.get((state, action), 0)
        max_future_q = max([self.q_table.get((next_state, a), 0) for a in valid_actions], default=0)
        new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.q_table[(state, action)] = new_q
        
    def printTable(self):
        print(self.q_table)
