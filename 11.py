import turtle

loadWindow = turtle.Screen()

turtle.speed(0)
turtle.bgcolor('black')
turtle.pencolor("#301e90") 

for i in range(50):

    turtle.circle(5*i)

    turtle.circle(-5*i)

    turtle.left(i)

 

turtle.exitonclick()