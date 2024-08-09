import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))

# Load and transform the turtle image
tt = pygame.image.load('turtle.png')
tt = pygame.transform.scale(tt, (75, 75))
angle = 0

x = []
w, l = 0, 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Move the turtle with WSAD and rotate with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                l -= 10
            if event.key == pygame.K_s:
                l += 10
            if event.key == pygame.K_a:
                w -= 10
            if event.key == pygame.K_d:
                w += 10
            if event.key == pygame.K_LEFT:
                angle -= 10
            if event.key == pygame.K_RIGHT:
                angle += 10

    pygame.display.update()
    screen.fill((55, 198, 255))

    # Rotate the turtle image
    rotated_tt = pygame.transform.rotate(tt, angle)
    # Calculate the new rect to keep the image centered
    new_rect = rotated_tt.get_rect(center=tt.get_rect(topleft=(w, l)).center)
    screen.blit(rotated_tt, new_rect.topleft)