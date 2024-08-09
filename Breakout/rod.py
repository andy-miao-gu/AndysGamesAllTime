import turtle 

class Rod(turtle.Turtle):
    def __init__(self):
        self.is_left = False
        self.is_right = False

    def make_rod(self):
        self.rod = turtle.Turtle()
        self.rod.shape('square')
        self.rod.shapesize(stretch_wid=1, stretch_len=5)
        self.rod.penup()
        self.rod.goto(0, -300)
        self.rod.color('black')

    def move_left(self):
        if self.is_left == True:
            self.rod.bk(3)
            if self.rod.xcor() < -325:
                self.rod.goto(-300, -300)
            turtle.ontimer(self.move_left, 10)

    def move_right(self):
        if self.is_right == True:
            self.rod.fd(3)
            if self.rod.xcor() > 325:
                self.rod.goto(300,-300)
            turtle.ontimer(self.move_right, 10)


    def start_moving_left(self):
        self.is_left = True
        self.move_left()

    def stop_moving_left(self):
        self.is_left = False

    def start_moving_right(self):
        self.is_right = True
        self.move_right()

    def stop_moving_right(self):
        self.is_right = False


if __name__ == '__main__':
    start = Rod()
    start.make_rod()


    turtle.listen()
    turtle.onkeypress(start.start_moving_left, 'Left')
    turtle.onkeyrelease(start.stop_moving_left, 'Left')



    turtle.onkeypress(start.start_moving_right, 'Right')
    turtle.onkeyrelease(start.stop_moving_right, 'Right')





    
    turtle.mainloop()
