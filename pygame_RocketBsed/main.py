import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Load images
background_image = pygame.image.load('andy.jpg')
rocket_image = pygame.image.load('rkt.png')
bullet_image = pygame.image.load('bullet.png')
falling_image = pygame.image.load('falling.png')  # Load your falling object image

# Scale the background to fit the screen
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Rocket scale factor
rocket_scale = 0.2  # Scale down to 50% of the original size; adjust this value as needed

# Scale the rocket
rocket_image = pygame.transform.scale(rocket_image, (int(rocket_image.get_width() * rocket_scale), int(rocket_image.get_height() * rocket_scale)))

# Get rocket dimensions
rocket_width = rocket_image.get_width()
rocket_height = rocket_image.get_height()

# Bullet scale factor
bullet_scale = 0.2  # Scale down the bullet; adjust this value as needed

# Scale the bullet
bullet_image = pygame.transform.scale(bullet_image, (int(bullet_image.get_width() * bullet_scale), int(bullet_image.get_height() * bullet_scale)))

# Get bullet dimensions
bullet_width = bullet_image.get_width()
bullet_height = bullet_image.get_height()

# Falling object scale factor
falling_scale = 0.5  # Scale down the falling object; adjust this value as needed

# Scale the falling object
falling_image = pygame.transform.scale(falling_image, (int(falling_image.get_width() * falling_scale), int(falling_image.get_height() * falling_scale)))

# Get falling object dimensions
falling_width = falling_image.get_width()
falling_height = falling_image.get_height()

# Starting position of the rocket
rocket_x = SCREEN_WIDTH // 2 - rocket_width // 2
rocket_y = SCREEN_HEIGHT - rocket_height - 10

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rocket Game')

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# List to keep track of bullets and falling objects
bullets = []
falling_objects = []

# Bullet speed
bullet_speed = 7

# Falling object speed
falling_speed = 5

# Score
score = 0

# Font for displaying score
font = pygame.font.Font(None, 36)

# Function to create a new falling object
def create_falling_object():
    x = random.randint(0, SCREEN_WIDTH - falling_width)
    y = -falling_height
    falling_objects.append([x, y])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new bullet
                bullet_x = rocket_x + rocket_width // 2 - bullet_width // 2
                bullet_y = rocket_y
                bullets.append([bullet_x, bullet_y])

    # Get the set of keys pressed
    keys = pygame.key.get_pressed()

    # Update rocket position based on key presses
    if keys[pygame.K_LEFT]:
        rocket_x -= 5
    if keys[pygame.K_RIGHT]:
        rocket_x += 5

    # Prevent the rocket from going out of bounds
    if rocket_x < 0:
        rocket_x = 0
    if rocket_x > SCREEN_WIDTH - rocket_width:
        rocket_x = SCREEN_WIDTH - rocket_width

    # Update bullet positions
    for bullet in bullets:
        bullet[1] -= bullet_speed  # Move the bullet up
        # Remove bullets that are off the screen
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Update falling object positions
    for falling_object in falling_objects:
        falling_object[1] += falling_speed  # Move the object down
        # Remove falling objects that are off the screen
        if falling_object[1] > SCREEN_HEIGHT:
            falling_objects.remove(falling_object)

    # Collision detection
    for bullet in bullets:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
        for falling_object in falling_objects:
            falling_rect = pygame.Rect(falling_object[0], falling_object[1], falling_width, falling_height)
            if bullet_rect.colliderect(falling_rect):
                bullets.remove(bullet)
                falling_objects.remove(falling_object)
                score += 1
                break

    # Create new falling objects periodically
    if random.randint(1, 50) == 1:  # Adjust frequency as needed
        create_falling_object()

    # Draw everything
    screen.blit(background_image, (0, 0))
    screen.blit(rocket_image, (rocket_x, rocket_y))
    for bullet in bullets:
        screen.blit(bullet_image, (bullet[0], bullet[1]))
    for falling_object in falling_objects:
        screen.blit(falling_image, (falling_object[0], falling_object[1]))

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
