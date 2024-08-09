import turtle
class ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.goto(0,0)
        self.dx = 4
        self.dy = 4

    # if the position of x is 325 then bounce or if x is -325 then bounce opposite direction sideway not upward
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)


    def bounce(self):
        self.dy *= -1

    def wall_bounce(self):
        self.dx *= -1

if __name__ == '__main__':
    start = ball()
    while (True):
        
        start.move()
        if start.xcor() > 325 or start.xcor() < -325:
            start.wall_bounce()
        if start.ycor() > 305 or start.ycor() < -305:
            start.bounce()
        
    turtle.mainloop()