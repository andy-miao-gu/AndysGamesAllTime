import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plants vs. Zombies")

# Define colors
WHITE = (255, 255, 255)

# Load images
background_image = pygame.image.load("background.jpg")
peashooter_image = pygame.image.load("peashooter.png")
zombie_image = pygame.image.load("zombie.png")

# Define classes
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = peashooter_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = zombie_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randint(1, 3)

# Set up groups
all_sprites = pygame.sprite.Group()
plants = pygame.sprite.Group()
zombies = pygame.sprite.Group()

# Add plants
plant = Plant(100, 500)
all_sprites.add(plant)
plants.add(plant)

# Main game loop
running = True
clock = pygame.time.Clock()
spawn_counter = 0
spawn_frequency = 100  # Adjust as needed

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn zombies
    spawn_counter += 1
    if spawn_counter >= spawn_frequency:
        zombie = Zombie()
        all_sprites.add(zombie)
        zombies.add(zombie)
        spawn_counter = 0

    # Update sprites
    all_sprites.update()

    # Draw everything
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Refresh display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
