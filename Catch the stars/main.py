import pgzrun
import random

WIDTH = 800
HEIGHT = 600

player = Actor("andy.png")
player.pos = WIDTH / 2, HEIGHT - 50

stars = []
score = 0

# Keep track of which keys are currently being pressed
keys_pressed = set()

def draw():
    screen.clear()
    player.draw()
    for star in stars:
        star.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

def update():
    global score
    for star in stars:
        star.y += 3
        if star.colliderect(player):
            stars.remove(star)
            score += 1

    # Add new stars
    if random.randint(1, 100) < 10:
        star = Actor("star.png")
        star.pos = random.randint(50, WIDTH - 50), 0
        stars.append(star)

    # Update player position based on keys pressed
    if keys_pressed:
        if keys.LEFT in keys_pressed:
            player.x -= 5  # Adjust the speed as needed
        if keys.RIGHT in keys_pressed:
            player.x += 5  # Adjust the speed as needed

def on_key_down(key):
    keys_pressed.add(key)

def on_key_up(key):
    keys_pressed.discard(key)

pgzrun.go()
