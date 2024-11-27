#import numpy as np
import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_winner = None

    def reset(self):
        self.board = [' '] * 9
        self.current_winner = None
        return self.get_state()

    def get_state(self):
        return ''.join(self.board)

    def available_actions(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def play_move(self, action, player):
        if self.board[action] == ' ':
            self.board[action] = player
            if self.check_winner(player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, player):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6],            # Diagonals
        ]
        for positions in winning_positions:
            if all(self.board[i] == player for i in positions):
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board

    def render(self):
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i+3]))
        print()

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state, available_actions):
        if random.random() < self.epsilon:  # Exploration
            return random.choice(available_actions)
        # Exploitation
        qs = [self.get_q(state, a) for a in available_actions]
        max_q = max(qs)
        return available_actions[qs.index(max_q)]

    def update_q(self, state, action, reward, next_state, next_actions):
        old_q = self.get_q(state, action)
        future_q = max([self.get_q(next_state, a) for a in next_actions], default=0.0)
        self.q_table[(state, action)] = old_q + self.alpha * (reward + self.gamma * future_q - old_q)

# Train the agent
def train_agent(episodes=10000):
    agent = QLearningAgent()
    opponent = QLearningAgent(epsilon=0.5)  # Opponent is also learning but explores more
    env = TicTacToe()

    for episode in range(episodes):
        state = env.reset()
        done = False
        turn = 'X'

        while not done:
            if turn == 'X':  # Agent's turn
                action = agent.choose_action(state, env.available_actions())
            else:  # Opponent's turn
                action = opponent.choose_action(state, env.available_actions())

            env.play_move(action, turn)
            next_state = env.get_state()
            reward = 0

            if env.current_winner == 'X':  # Agent wins
                reward = 1
                done = True
            elif env.current_winner == 'O':  # Opponent wins
                reward = -1
                done = True
            elif env.is_draw():  # Draw
                reward = 0.5
                done = True

            if turn == 'X':
                agent.update_q(state, action, reward, next_state, env.available_actions())
            else:
                opponent.update_q(state, action, -reward, next_state, env.available_actions())

            state = next_state
            turn = 'O' if turn == 'X' else 'X'

        if (episode + 1) % 1000 == 0:
            print(f"Episode {episode + 1}/{episodes}")

    return agent

# Test the agent
def play_with_agent(agent):
    env = TicTacToe()
    state = env.reset()
    done = False
    turn = 'X'

    print("Starting a new game!")
    env.render()

    while not done:
        if turn == 'X':  # Player
            action = int(input(f"Choose your action (0-8): "))
        else:  # Agent
            action = agent.choose_action(state, env.available_actions())

        if env.play_move(action, turn):
            state = env.get_state()
            env.render()

            if env.current_winner:
                print(f"{turn} wins!")
                done = True
            elif env.is_draw():
                print("It's a draw!")
                done = True

            turn = 'O' if turn == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Train and play
if __name__ == "__main__":
    trained_agent = train_agent(episodes=1000000)
    
    with open("text.txt", "w") as file:
        print("Length: ", len(trained_agent.q_table), file=file)
        for key, value in trained_agent.q_table.items():
            print(f"{key[0][0]}|{key[0][1]}|{key[0][2]}\n{key[0][3]}|{key[0][4]}|{key[0][5]}      ,Pos: {key[1]} , Value: {value}\n{key[0][6]}|{key[0][7]}|{key[0][8]}\n\n", file=file)
    #play_with_agent(trained_agent)
