import turtle
from mycar import AndyCar
from mutipleCars import MultiCar
import time

screen = turtle.Screen()
turtle.register_shape("abc_small3.gif")
turtle.tracer(0)
car = AndyCar()
car.listen_button()
mc = MultiCar()
while (True):
    turtle.Screen().update()
    for i in mc.list_of_cars:
        i.forward(5)
        distanace = abs(   (  (i.xcor() - car.xcor())**2 + (i.ycor() - car.ycor())**2 )**0.5    )
        print(distanace)
        if  distanace<68:
            print("Game Over",distanace) 
            turtle.done()
            

    time.sleep(0.1)
    mc.ratimcame()


    

turtle.mainloop()