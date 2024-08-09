import turtle as t
import time
from snake import Snake
from food import Food

t.screensize(600, 600)
t.bgcolor("black")


t.tracer(0)
s = Snake()
f = Food()
while True:
    
    s.move()
    # move based onkeys

    #move based on keys
    s.listen_keys()
    t.Screen().update()
    #detect collision with food
    if s.segments[0].distance(f) < 25:
        f.refresh()
        s.extend()
    #detect collision with wall
    if s.segments[0].xcor() > 340 or s.segments[0].xcor() < -340 or s.segments[0].ycor() > 340 or s.segments[0].ycor() < -340:
        t.done()
    #detect collision with tail
    for i in s.segments[1:]:
        if s.segments[0].distance(i) < 10:
            t.done()
            

    time.sleep(0.1)





t.done()

    