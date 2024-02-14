import os

os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

import pygame
import random


# 游戏区域大小
WIDTH = 800
HEIGHT = 600
FPS = 30

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# 方块大小
BLOCK_SIZE = 30

# 初始化Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("俄罗斯方块")
clock = pygame.time.Clock()

# 方块形状定义
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

# 方块颜色定义
COLORS = [CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, ORANGE]

# 游戏区域矩阵
grid = [[0] * (WIDTH // BLOCK_SIZE) for _ in range(HEIGHT // BLOCK_SIZE)]

# 创建一个方块
def create_block():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    x = (WIDTH // BLOCK_SIZE) // 2 - len(shape[0]) // 2
    y = 0
    return shape, color, x, y

# 绘制方块
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

# 绘制游戏区域
def draw_grid():
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                draw_block(x, y, COLORS[cell - 1])

# 检查方块是否与游戏区域发生碰撞
def check_collision(shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
           if shape[row][col] and (y + row >= len(grid) or x + col < 0 or x + col >= len(grid[0]) or grid[y + row][x + col]):
                return True
    return False

# 将方块合并到游戏区域
def merge_block(shape, x, y, color):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                grid[y + row][x + col] = color

# 消除满行
def clear_lines():
    full_rows = [row for row in range(len(grid)) if all(grid[row])]
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * (WIDTH // BLOCK_SIZE))

# 游戏主循环
def game_loop():
    running = True
    current_block = create_block()
    next_block = create_block()
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(current_block[0], current_block[2] - 1, current_block[3]):
                        current_block = (current_block[0], current_block[1], current_block[2] - 1, current_block[3])
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(current_block[0], current_block[2] + 1, current_block[3]):
                        current_block = (current_block[0], current_block[1], current_block[2] + 1, current_block[3])
                elif event.key == pygame.K_DOWN:
                    if not check_collision(current_block[0], current_block[2], current_block[3] + 1):
                        current_block = (current_block[0], current_block[1], current_block[2], current_block[3] + 1)
                elif event.key == pygame.K_SPACE:
                    shape, color, x, y = current_block
                    while not check_collision(shape, x, y + 1):
                        y += 1
                    current_block = (shape, color, x, y)

        shape, color, x, y = current_block
        if not check_collision(shape, x, y + 1):
            current_block = (shape, color, x, y + 1)
        else:
            merge_block(shape, x, y, COLORS.index(color) + 1)
            clear_lines()
            if check_collision(next_block[0], next_block[2], next_block[3]):
                running = False
            current_block = next_block
            next_block = create_block()
            score += 10

        screen.fill(BLACK)
        draw_grid()
        for row in range(len(next_block[0])):
            for col in range(len(next_block[0][row])):
                if next_block[0][row][col]:
                    draw_block(col + 12, row + 2, next_block[1])
        pygame.display.flip()
        clock.tick(FPS)

    print("游戏结束！你的得分是：", score)

# 运行游戏
game_loop()