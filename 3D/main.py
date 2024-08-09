import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Define the vertices and edges of a smaller cube
vertices = [
    [0.25, 0.25, -0.25],
    [0.25, -0.25, -0.25],
    [-0.25, -0.25, -0.25],
    [-0.25, 0.25, -0.25],
    [0.25, 0.25, 0.25],
    [0.25, -0.25, 0.25],
    [-0.25, -0.25, 0.25],
    [-0.25, 0.25, 0.25]
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

surfaces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (1, 2, 6, 5),
    (4, 7, 3, 0)
]

colors = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1)
]

def draw_cube():
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(60, (display[0] / display[1]), 0.1, 50.0)  # Increased the field of view (from 45 to 60)
    glTranslatef(0.0, -1.5, -5)  # Adjust initial position for a closer view, slightly upwards

    player_pos = [0.0, 0.0, 0.0]
    player_angle = 10  # Adjust the initial angle for a diagonal view
    jump = False
    jump_height = 0.1
    gravity = -0.02
    y_velocity = 0
    player_pitch = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            player_angle += 2
        if keys[pygame.K_RIGHT]:
            player_angle -= 2
        if keys[pygame.K_UP]:
            player_pitch += 2  # Adjust pitch upwards
        if player_pitch > 90:
                player_pitch = 90
        if keys[pygame.K_DOWN]:
            player_pitch -= 2  # Adjust pitch downwards
            if player_pitch < -90:
                player_pitch = -90
        if keys[pygame.K_w]:
            player_pos[0] -= 0.05 * math.sin(math.radians(player_angle))
            player_pos[2] -= 0.05 * math.cos(math.radians(player_angle))
        if keys[pygame.K_s]:
            player_pos[0] += 0.05 * math.sin(math.radians(player_angle))
            player_pos[2] += 0.05 * math.cos(math.radians(player_angle))
        if keys[pygame.K_a]:
            player_pos[0] -= 0.05 * math.cos(math.radians(player_angle))
            player_pos[2] += 0.05 * math.sin(math.radians(player_angle))
        if keys[pygame.K_d]:
            player_pos[0] += 0.05 * math.cos(math.radians(player_angle))
            player_pos[2] -= 0.05 * math.sin(math.radians(player_angle))
        if keys[pygame.K_SPACE]:
            if not jump:
                jump = True
                y_velocity = jump_height

        # Apply gravity
        if jump:
            player_pos[1] += y_velocity
            y_velocity += gravity
            if player_pos[1] <= 0:
                player_pos[1] = 0
                jump = False
                y_velocity = 0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(60, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(player_pos[0], player_pos[1], player_pos[2] - 10)
        glRotatef(player_pitch, 1, 0, 0)
        glRotatef(player_angle, 0, 1, 0)
        draw_cube()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
