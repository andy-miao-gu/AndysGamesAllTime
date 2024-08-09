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
PIPE_GAP = 200  # Increase the gap between pipes
GROUND_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Andy")

# Load images (replace 'your_face.png' with the path to your face image)
bird_image = pygame.Surface((50, 50))  # Temporary surface for the bird

# Bird color
bird_image.fill(RED)  # Red color for the bird

# New Constants
HEARTS = 5  # Number of hearts
FONT = pygame.font.Font(None, 36)  # Font for displaying hearts

# Bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        self.velocity = 0
        self.hearts = HEARTS  # Adding hearts counter
        self.collide_time = 0
        self.is_colliding = False
        self.is_blurred = False
        self.blur_amount = 0

    def update(self):
        if self.is_colliding:
            if self.collide_time < 10:
                # Flash black and white
                if self.collide_time % 2 == 0:
                    self.image.fill(WHITE)
                else:
                    self.image.fill(BLACK)
                self.collide_time += 1
            else:
                # Start blurring effect
                if not self.is_blurred:
                    self.blur_amount += 1
                    self.image.set_alpha(255 - self.blur_amount * 5)
                    self.image = pygame.transform.scale(self.image, (55, 55))
                    if self.blur_amount >= 50:
                        self.is_blurred = True
                else:
                    self.image.set_alpha(255 - self.blur_amount * 5)
                    self.image = pygame.transform.scale(self.image, (55, 55))
        else:
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
        self.image.fill(BLACK)
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

    hearts_text = FONT.render("Hearts: " + str(bird.hearts), True, RED)

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

        # Pipe collision check
        for pipe in pipes:
            if pygame.sprite.collide_rect(bird, pipe):
                bird.is_colliding = True
                bird.collide_time = 0
                bird.hearts -= 1
                hearts_text = FONT.render("Hearts: " + str(bird.hearts), True, RED)
                if bird.hearts <= 0:
                    running = False  # Game over when no hearts left

        # Update sprites
        all_sprites.update()

        # Drawing
        screen.fill(WHITE)
        all_sprites.draw(screen)
        screen.blit(hearts_text, (10, 10))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
