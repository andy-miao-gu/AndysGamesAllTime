import pgzrun

# Game window size
WIDTH = 700
HEIGHT = 480

# Game variables
bird = Actor('andy', (75, 350))
bird.velocity = 0
GRAVITY = 0.3
FLAP_STRENGTH = -3
game_over = False

# Load background image
BACKGROUND = 'bg'
bird.images = ['andy']

# Resizing the bird to 10% of its original size
bird.width //= 10
bird.height //= 10

def draw():
    screen.blit(BACKGROUND, (0, 0))
    bird.draw()

def update():
    global game_over

    if not game_over:
        update_bird()

def update_bird():
    global game_over

    bird.y += bird.velocity
    bird.velocity += GRAVITY

    # No pipe collision checking since pipes are removed

def on_key_down():
    if not game_over:
        bird.velocity = FLAP_STRENGTH

pgzrun.go()
