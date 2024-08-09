import pygame as pg
import random
# Initialize the grid


# Initialize Pygame
pg.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 25
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
grid = [[0] * GRID_HEIGHT for _ in range(GRID_WIDTH)]
# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 1]],
    
]

SHAPES_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Initialize screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tetris")

# Function to create a new Tetromino
def new_tetromino():
    shape = random.choice(SHAPES)
    color = random.choice(SHAPES_COLORS)
    tetromino = {
        "shape": shape,
        "color": color,
        "x": GRID_WIDTH // 2 - len(shape[0]) // 2,
        "y": 0
    }
    return tetromino

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pg.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pg.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Function to draw a Tetromino
def draw_tetromino(tetromino):
    shape = tetromino["shape"]
    color = tetromino["color"]
    x, y = tetromino["x"], tetromino["y"]

    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col]:
                pg.draw.rect(screen, color, (x + col * GRID_SIZE, y + row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Main game loop
clock = pg.time.Clock()
running = True
current_tetromino = new_tetromino()
fall_speed = 1
fall_counter = 0

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                current_tetromino["x"] -= 1
            if event.key == pg.K_RIGHT:
                current_tetromino["x"] += 1

    # Move the Tetromino down
    fall_counter += 1
    if fall_counter >= fall_speed:
        current_tetromino["y"] += 1
        fall_counter = 0

    # Collision detection
    for row in range(len(current_tetromino["shape"])):
        for col in range(len(current_tetromino["shape"][0])):
            if current_tetromino["shape"][-row][-col]:
                if (current_tetromino["y"] + row >= GRID_HEIGHT or
                        current_tetromino["x"] + col < 0 or
                        current_tetromino["x"] + col >= GRID_WIDTH):
                    current_tetromino = new_tetromino()

    # Clear rows
    rows_to_clear = []
    for row in range(GRID_HEIGHT):
        if all([grid[col][row] for col in range(GRID_WIDTH)]):
            rows_to_clear.append(row)

    for row in rows_to_clear:
        for col in range(GRID_WIDTH):
            grid[col].pop(row)
            grid[col].insert(0, 0)

    # Drawing
    screen.fill(BLACK)
    draw_grid()
    draw_tetromino(current_tetromino)
    pg.display.flip()

    clock.tick(60)

pg.quit()
