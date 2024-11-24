import pygame
from utils.constants import GRID_SIZE, CELL_SIZE, WHITE, SCREEN_WIDTH

class Board():
    def __init__(self):
        self.grid = [[ '' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        # self.grid = [['X','O','X'],
        #              ['X','O','O'],
        #              ['X','X','X']]
        
    def draw(self, screen, player):
        screen.blit(pygame.font.Font(None, 40).render(player, True, WHITE), (SCREEN_WIDTH // 2 - 45, 5))
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x, y = row*CELL_SIZE, col*CELL_SIZE
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE), 3)
                if self.grid[row][col]:
                    font = pygame.font.Font(None, 150)
                    text = font.render(self.grid[row][col], True, WHITE)
                    screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 3.1, row * CELL_SIZE + CELL_SIZE // 3.75))
                    
    def update(self, x, y, symbol):
        self.grid[y // 200][x // 200] = symbol