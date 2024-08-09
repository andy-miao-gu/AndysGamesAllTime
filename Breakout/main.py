import turtle 
from rod import Rod
from ball import ball
from Bricks import Bricks

turtle.tracer(0, 0)

brick = Bricks()
brick.make_brick()

rod = Rod()
rod.make_rod()

turtle.listen()
turtle.onkeypress(rod.start_moving_left, 'Left')
turtle.onkeyrelease(rod.stop_moving_left, 'Left')

turtle.onkeypress(rod.start_moving_right, 'Right')
turtle.onkeyrelease(rod.stop_moving_right, 'Right')


ball = ball()
while (True):
    
    # stop ball from going outside and bouding
    ball.move()
    if ball.xcor() > 325 or ball.xcor() < -325:
        ball.wall_bounce()
    if ball.ycor() > 305 :
        ball.bounce()

    if ball.ycor() < -325:
        break 
        turtle.done()


    # collion with rod 
    if rod.rod.ycor() - 20 < ball.ycor() < rod.rod.ycor() + 20:
        if rod.rod.distance(ball) < 45:
            ball.bounce()
        
    

    # collision with bricks
    for b in brick.all_bricks:
        if b.ycor() - 20 < ball.ycor() < b.ycor() + 20:
            if b.distance(ball) < 45:
                ball.bounce()
                b.hideturtle()
                brick.all_bricks.remove(b)
                

    




    turtle.update()
        
turtle.mainloop()