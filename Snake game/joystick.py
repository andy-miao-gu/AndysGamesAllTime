import pygame

# Initialize Pygame
pygame.init()

# Check for connected joysticks
joystick_count = pygame.joystick.get_count()

if joystick_count > 0:
    # Initialize the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Get the x and y positions of the joystick
    x_axis = joystick.get_axis(0)  # X-axis position (-1 to 1)
    y_axis = joystick.get_axis(1)  # Y-axis position (-1 to 1)

    print("X-axis position:", x_axis)
    print("Y-axis position:", y_axis)
else:
    print("No joystick connected")
