import tkinter as tk
import random
import time
import threading

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Counter")
        self.root.geometry("300x200")

        self.count = 0
        self.highest_score = 0

        self.label = tk.Label(self.root, text="Count: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Click me!", command=self.change_count, font=("Helvetica", 14))
        self.button.pack(pady=20)

        self.is_green = True
        self.green_screen()
        self.start_time = time.time()
        self.game_duration = 20  # Game duration in seconds

        self.random_red_thread = threading.Thread(target=self.random_red)
        self.random_red_thread.daemon = True
        self.random_red_thread.start()

        self.root.after(self.game_duration * 1000, self.end_game)  # End game after 20 seconds

    def change_count(self):
        if self.is_green:
            self.count += 1
        else:
            self.count -= 10
        self.label.config(text=f"Count: {self.count}")

    def green_screen(self):
        self.is_green = True
        self.root.config(bg="green")
        self.button.config(state=tk.NORMAL)

    def red_screen(self):
        self.is_green = False
        self.root.config(bg="red")
        self.button.config(state=tk.NORMAL)
        self.root.after(1000, self.green_screen)  # Return to green after 1 second

    def random_red(self):
        while True:
            time.sleep(random.randint(10, 25))  # Randomly sleep for 10 to 25 seconds
            self.root.after(0, self.red_screen)  # Switch to red screen on the main thread

    def end_game(self):
        self.highest_score = max(self.highest_score, self.count)
        self.label.config(text=f"Final Count: {self.count}\nHighest Score: {self.highest_score}")
        self.button.config(state=tk.DISABLED)
        self.root.config(bg="white")
        self.random_red_thread.join(0)  # Stop the red screen thread

import tkinter as tk
import random
import time
import threading

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Counter")
        self.root.geometry("300x200")

        self.count = 0
        self.highest_score = 0

        self.label = tk.Label(self.root, text="Count: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Click me!", command=self.change_count, font=("Helvetica", 14))
        self.button.pack(pady=20)

        self.is_green = True
        self.green_screen()
        self.start_time = time.time()
        self.game_duration = 20  # Game duration in seconds

        self.random_red_thread = threading.Thread(target=self.random_red)
        self.random_red_thread.daemon = True
        self.random_red_thread.start()

        self.root.after(self.game_duration * 1000, self.end_game)  # End game after 20 seconds

    def change_count(self):
        if self.is_green:
            self.count += 1
        else:
            self.count -= 10
        self.label.config(text=f"Count: {self.count}")

    def green_screen(self):
        self.is_green = True
        self.root.config(bg="green")
        self.button.config(state=tk.NORMAL)

    def red_screen(self):
        self.is_green = False
        self.root.config(bg="red")
        self.button.config(state=tk.NORMAL)
        self.root.after(1000, self.green_screen)  # Return to green after 1 second

    def random_red(self):
        while True:
            time.sleep(random.randint(1, 10))  # Randomly sleep for 10 to 25 seconds
            self.root.after(0, self.red_screen)  # Switch to red screen on the main thread

    def end_game(self):
        self.highest_score = max(self.highest_score, self.count)
        self.label.config(text=f"Final Count: {self.count}\nHighest Score: {self.highest_score}")
        self.button.config(state=tk.DISABLED)
        self.root.config(bg="white")
        self.random_red_thread.join(0)  # Stop the red screen thread

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()
