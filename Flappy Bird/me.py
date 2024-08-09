import tkinter as tk
import numpy as np

root = tk.Tk()
root.title('Flappy Andy')
root.geometry('400x400')

angimg = tk.PhotoImage(file='Safeimagekit-resized-img.png')

canvas = tk.Canvas(root, width=400, height=400)
canvas.create_image(0, 0, anchor=tk.NW, image=angimg)

andy_img = tk.PhotoImage(file='Me as flappy.png')
bird = canvas.create_image(50, 200, anchor=tk.NW, image=andy_img)
canvas.pack()

gravity = 0.19999
y_speed = 0
jump_speed = -5.5


def jump(event):
    global y_speed
    y_speed = jump_speed


root.bind("<space>", jump)

pipe_width = 50
pipe_height = np.random.randint(100, 160)


def move_pipe():
    global pipe
    canvas.move(pipe, -5, 0)
    pos = get_pipe_coordinates(pipe)
    if any(pos) < 0:
        reset_pipe_position()
    root.after(10, move_pipe)


def reset_pipe_position():
    canvas.coords(pipe, 400, 0, 400 + pipe_width, pipe_height)


pipe = canvas.create_rectangle(400, 0, 400 + pipe_width, pipe_height, fill='green')


def get_pipe_coordinates(pipe):
    return canvas.coords(pipe)


def move_pipe2():
    canvas.move(pipe2, -3, 0)
    root.after(10, move_pipe2)


pipe2 = canvas.create_rectangle(400, 0, 400 + pipe_width, pipe_height, fill='black')


def update():
    global y_speed
    bird_coords = canvas.coords(bird)

    y_speed = y_speed + gravity
    canvas.move(bird, 0, y_speed)

    root.after(10, update)


move_pipe()
move_pipe2()

root.after(10, update)

root.mainloop()
 