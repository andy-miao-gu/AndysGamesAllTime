import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
FPS = 60
GRAVITY = 0.5
JUMP_SPEED = -8  # Adjust the jump height
PIPE_WIDTH = 70
PIPE_GAP = 200   # Increase the gap between pipes
GROUND_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set up window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Andy")

# Load images (replace 'your_face.png' with the path to your face image)
bird_image = pygame.image.load("Me as flappy.png").convert_alpha()  # Replace with your face image
bird_image = pygame.transform.scale(bird_image, (50, 50))  # Adjust size as needed

# Bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = HEIGHT - GROUND_HEIGHT
            self.velocity = 0

    def jump(self):
        self.velocity = JUMP_SPEED

# Pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, height):
        super().__init__()
        self.image = pygame.Surface((PIPE_WIDTH, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

# Main game function
def main():
    bird = Bird()
    all_sprites = pygame.sprite.Group()
    pipes = pygame.sprite.Group()
    all_sprites.add(bird)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Pipe generation
        if random.randint(1, 60) == 1:
            top_height = random.randint(50, 200)
            bottom_height = HEIGHT - top_height - PIPE_GAP
            new_pipe_top = Pipe(WIDTH, 0, top_height)
            new_pipe_bottom = Pipe(WIDTH, HEIGHT - bottom_height, bottom_height)
            pipes.add(new_pipe_top)
            pipes.add(new_pipe_bottom)
            all_sprites.add(new_pipe_top)
            all_sprites.add(new_pipe_bottom)

        # Update sprites
        all_sprites.update()

        # Drawing
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
