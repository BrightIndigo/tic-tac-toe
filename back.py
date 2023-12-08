import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

clock = pygame.time.Clock()

board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def draw_grid():
    cell_size = WIDTH // 3
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * cell_size), (WIDTH, i * cell_size), 2)
        pygame.draw.line(screen, LINE_COLOR, (i * cell_size, 0), (i * cell_size, HEIGHT), 2)

def draw_symbol(row, col):
    cell_size = WIDTH // 3
    margin = 20

    x = col * cell_size + margin
    y = row * cell_size + margin

    if board[row][col] == 'X':
        pygame.draw.line(screen, LINE_COLOR, (x, y), (x + cell_size - 2 * margin, y + cell_size - 2 * margin), 2)
        pygame.draw.line(screen, LINE_COLOR, (x, y + cell_size - 2 * margin), (x + cell_size - 2 * margin, y), 2)
    elif board[row][col] == 'O':
        pygame.draw.circle(screen, LINE_COLOR, (x + cell_size // 2 - 18, y + cell_size // 2 - 18), cell_size // 2 - margin, 2)

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def check_draw():
    return all(board[i][j] != '' for i in range(3) for j in range(3))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_player == 'X':
                row = event.pos[1] // (HEIGHT // 3)
                col = event.pos[0] // (WIDTH // 3)
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                    board[row][col] = 'X'
                    if check_win():
                        print("Player X wins!")
                        running = False
                    elif check_draw():
                        print("It's a draw!")
                        running = False
                    else:
                        current_player = 'O'
            else:
                row = event.pos[1] // (HEIGHT // 3)
                col = event.pos[0] // (WIDTH // 3)
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                    board[row][col] = 'O'
                    if check_win():
                        print("Player O wins!")
                        running = False
                    elif check_draw():
                        print("It's a draw!")
                        running = False
                    else:
                        current_player = 'X'

    screen.fill(WHITE)

    draw_grid()

    for i in range(3):
        for j in range(3):
            draw_symbol(i, j)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
