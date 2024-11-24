from utils.constants import GRID_SIZE

class GameEngine():
    def __init__(self) -> None:
        self.currentPlayer = None
        
    def switchPlayer(self, player1, player2):
        self.currentPlayer = player1 if self.currentPlayer == player2 else player2
        
    def checkWinner(self, board):
        grid = board.grid
        
        for row in grid:
            if row[0] and all(ele == row[0] for ele in row):
                return row[0]
            
        for col in range(GRID_SIZE):
            if grid[0][col] and all(grid[row][col] == grid[0][col] for row in range(GRID_SIZE)):
                return grid[0][col]
            
        if grid[0][0] and all(grid[i][i] == grid[0][0] for i in range(GRID_SIZE)):
            return grid[0][0]
        
        if grid[0][0] and all(grid[i][2-i] == grid[0][0] for i in range(GRID_SIZE)):
            return grid[0][0]
        
        return None

