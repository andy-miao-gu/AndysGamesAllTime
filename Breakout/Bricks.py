import turtle
class Bricks(turtle.Turtle):
    def __init__(self):
        pass

    def make_single_brick(self, x, y,color):
        self.brick = turtle.Turtle()
        self.brick.shape('square')
        self.brick.shapesize(stretch_wid=1, stretch_len=2.9)
        self.brick.penup()
        self.brick.goto(x, y)
        self.brick.color(color)
        return self.brick

    def make_brick(self,x_bricks=[ -325,-260, -195, -130, -65, 0, 65, 130, 195, 260, 325]):
        self.xBrick = x_bricks
        #make space between bricks from -300 to 300
        list_of_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', "pink"]
        
        i = 0
        self.all_bricks = []
        for x in self.xBrick:
            color = list_of_colors[i%7]
            for y in range(225,300,25):
                b = self.make_single_brick(x, y,color)
                self.all_bricks.append(b)
            i = i + 1
    


if __name__ == '__main__':
    start = Bricks()
    start.make_brick()
    
    turtle.mainloop()