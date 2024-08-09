import tkinter as tk
import random

# Function to handle the jump when the space key is pressed
def jump(event):
    global y_speed
    y_speed = jump_speed

# Function to update the position of the bird and check for collisions
def update():
    global y_speed

    # Get the current coordinates of the bird
    bird_coords = canvas.coords(bird)

    # Update the bird's vertical speed due to gravity
    y_speed = y_speed + gravity

    # Move the bird based on the current speed
    canvas.move(bird, 0, y_speed)

    # Check for collisions with pipes
    check_collision()

    # Schedule the next update after 10 milliseconds
    root.after(10, update)

# Function to check for collisions with pipes
def check_collision():
    bird_coords = canvas.coords(bird)

    for pipe in pipes:
        pipe_coords = canvas.coords(pipe)

        # Check if the bird overlaps with any pipe
        if (
            bird_coords[2] > pipe_coords[0]
            and bird_coords[0] < pipe_coords[2]
            and (bird_coords[3] > pipe_coords[1] or bird_coords[1] < pipe_coords[3])
        ):
            print("Collision!")
            root.destroy()

# Function to create a new pipe
def create_pipe():
    pipe_height = random.randint(pipe_height_range[0], pipe_height_range[1])
    pipe = canvas.create_rectangle(
        400, 0, 400 + pipe_width, pipe_height, fill="green"
    )
    pipes.append(pipe)

# Function to move all pipes and check for creating new pipes
def move_pipes():
    for pipe in pipes:
        canvas.move(pipe, pipe_speed, 0)

    check_and_create_pipe()

    # Schedule the next pipe movement after 10 milliseconds
    root.after(10, move_pipes)

# Function to check and create a new pipe as needed
def check_and_create_pipe():
    if pipes and canvas.coords(pipes[0])[2] < 0:
        canvas.delete(pipes.pop(0))

    if len(pipes) < 2:
        create_pipe()

# Create the main Tkinter window
root = tk.Tk()
root.title('Flappy Bird by YourName')  # Replace 'YourName' with your actual name
root.geometry('400x400')

# Load the bird image and background image
angimg = tk.PhotoImage(file='Safeimagekit-resized-img.png')
bird_image = tk.PhotoImage(file='Me as flappy.png')

# Create a canvas to display the game elements
canvas = tk.Canvas(root, width=400, height=400)
canvas.create_image(0, 0, anchor=tk.NW, image=angimg)
bird = canvas.create_image(50, 200, anchor=tk.NW, image=bird_image)
canvas.pack()

# Set up game parameters
gravity = 0.19999
y_speed = 0
jump_speed = -5.5
pipe_width = 50
pipe_height_range = (100, 160)
pipe_speed = -2
pipes = []

# Bind the space key to the jump function
root.bind("<space>", jump)

# Schedule the initial update and pipe movement
root.after(10, update)
root.after(10, move_pipes)

# Start the Tkinter main loop
root.mainloop()
