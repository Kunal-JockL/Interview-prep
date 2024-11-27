import pygame
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, RED, BLUE, WHITE, GREEN
from game.board import Board
from game.player import Player
from game.engine import GameEngine
from rl.agent import RLAgent

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    
    board = Board()
    player1 = Player("Player 1", "X")
    agent = RLAgent("RLAgent","O")
    engine = GameEngine()
    engine.currentPlayer = player1
    
    clock = pygame.time.Clock()
    running = True
    winner = None
    
    while running:
        screen.fill(BLACK)
        board.draw(screen, engine.currentPlayer.name)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not winner and engine.currentPlayer == player1:
                agent.printTable()
                x, y = pygame.mouse.get_pos()
                if not board.grid[y // 200][x // 200]:
                    board.update(x, y, engine.currentPlayer.symbol)
                    winner = engine.checkWinner(board)
                    if not winner:
                        engine.switchPlayer(player1, agent)
            elif engine.currentPlayer == agent and not winner:
                agent.printTable()
                row, col = agent.choose_action(board)
                board.update(row, col, engine.currentPlayer.symbol)
                winner = engine.checkWinner(board)
                if not winner:
                    engine.switchPlayer(player1, agent)
                                        
        if winner:
            font = pygame.font.Font(None, 80)
            text = font.render(f"{engine.currentPlayer.name} Wins!", True, RED if winner == "X" else BLUE)
            screen.blit(text, (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 2.2))
            
        if all(ele for ele in [*board.grid[0], *board.grid[1], *board.grid[2]]) and not winner:
            font = pygame.font.Font(None, 80)
            text = font.render("Draw!", True, GREEN)
            screen.blit(text, (SCREEN_WIDTH // 2.7, SCREEN_HEIGHT // 2.2))
            
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
                
                
if __name__ == "__main__":
    main()