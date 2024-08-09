import turtle as t


class Snake:
    def __init__(self):   
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            tt = t.Turtle()
            if i ==0:
                tt.shape('turtle')
                tt.color("green")
            else:
                tt.shape('classic')
                tt.color("red")
                tt.shapesize(stretch_len=1, stretch_wid=1)
            tt.penup()
            tt.goto( -20 * i,0)
            self.segments.append(tt)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            #get heading
            heading = self.segments[0].heading()
            self.segments[i].goto(x, y)
            self.segments[i].setheading(heading)
        self.segments[0].forward(20)


    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
        

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

        
    def listen_keys(self):
        t.listen()
        t.onkey(self.up, "Up")
        t.onkey(self.down, "Down")
        t.onkey(self.left, "Left")
        t.onkey(self.right, "Right")   
       
    def extend(self):
        tt = t.Turtle()
        tt.shape('classic')
        tt.color("red")
        tt.penup()
        tt2 = t.Turtle()
        tt2.shape('triangle')
        tt2.color("red")
        tt2.penup()
        tt2.goto(tt.xcor() + 20, tt.ycor())

        self.segments.append(tt)
        self.segments.append(tt2)
