import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(1)
t.speed(15)


col =('#ED7864', '#6E544F', '#592F2F')
for i in range (300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)

s.exitonclick()