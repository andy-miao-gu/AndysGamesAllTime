import tkinter as tk

class MovingImageApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.image = tk.PhotoImage(file="/Users/andymiaogu/Desktop/Andy's coding/Games/Flappy bird pgzrun/check/images/andy.png")
        self.image_id = self.canvas.create_image(200, 200, image=self.image)
        self.canvas.focus_set()
        self.canvas.bind("<space>", self.move_up)
        self.gravity = 1
        self.dy = 0
        self.animate()

    def move_up(self, event):
        self.dy = -10  # Adjust this value for the speed of the upward movement

    def animate(self):
        self.canvas.move(self.image_id, 0, self.dy)
        self.dy += self.gravity

        # Get the coordinates of the image
        x1, y1, x2, y2 = self.canvas.bbox(self.image_id)

        # If the image hits the bottom, stop and reset its position
        if y2 >= 400:
            self.dy = 0
            self.canvas.move(self.image_id, 0, 400 - y2)

        self.master.after(20, self.animate)

root = tk.Tk()
app = MovingImageApp(root)
root.mainloop()
