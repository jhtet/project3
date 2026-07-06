import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Board settings
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS
board = [["" for _ in range(COLS)] for _ in range(ROWS)]

# Fonts
FONT = pygame.font.SysFont(None, 100)

# Game variables
current_player = "X"
game_over = False

def draw_board():
    WIN.fill(WHITE)
    # Draw grid lines
    pygame.draw.line(WIN, BLACK, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(WIN, BLACK, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(WIN, BLACK, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(WIN, BLACK, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

def draw_symbols():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != "":
                text = FONT.render(board[row][col], True, BLACK)
                x = col * CELL_SIZE + CELL_SIZE // 3
                y = row * CELL_SIZE + CELL_SIZE // 6
                WIN.blit(text, (x, y))

def check_winner():
    global game_over
    # Rows & Columns
    for i in range(ROWS):
        if board[i][0] == board[i][1] == board[i][2] != "":
            game_over = True
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            game_over = True
            return board[0][i]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        game_over = True
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        game_over = True
        return board[0][2]
    return None

def is_full():
    return all(board[row][col] != "" for row in range(ROWS) for col in range(COLS))

def main():
    global current_player
    clock = pygame.time.Clock()
    draw_board()
    winner = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if board[row][col] == "":
                    board[row][col] = current_player
                    winner = check_winner()
                    if not winner and not is_full():
                        current_player = "O" if current_player == "X" else "X"

        draw_board()
        draw_symbols()
        pygame.display.update()
        clock.tick(30)

        if winner:
            print(f"{winner} wins!")
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()
        elif is_full() and not winner:
            print("It's a tie!")
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
