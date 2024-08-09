import turtle

class AndyCar(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("abc_small3.gif")
        self.shapesize(0.1, 0.1)
        self.left(90)
        self.penup()
        self.goto(0, -300)

    def forward_now(self):
        self.forward(15)

    def backward_now(self):
        self.backward(15)

    def listen_button(self):
        turtle.listen()
        turtle.onkey(self.forward_now, "Up")
        turtle.onkey(self.backward_now, "Down")



