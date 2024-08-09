import turtle as ttl
import random
import time


class MultiCar():
    def __init__(self):
        super().__init__()
        self.list_of_cars = []
        self.shapes =['square', 'triangle', 'circle', 'turtle']
        self.colors = ["red", "blue", "green", "yellow", "purple", "orange", "black", "brown", "pink", "gray"]
    def ratimcame(self):
        if random.randint(1,50) == 1:
            tt = ttl.Turtle()
            tt.shape(random.choice(self.shapes))
            tt.shapesize(3, 3)
            tt.color(random.choice(self.colors))
            tt.penup()
            tt.goto(random.randint(-500, -400), random.randint(-200, 500))
            self.list_of_cars.append(tt)
        return self.list_of_cars

        
   
