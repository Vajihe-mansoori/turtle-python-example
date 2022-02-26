import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("#262626")
t.pencolor("#7C909C")
t.speed(100)


col =('#ED7864', '#6E544F', '#592F2F', '#6E382E')
for N in range (5):
    for X in range (8):
        t.speed(X+10)
        for X in range (2):
            t.pensize(2)
            t.circle(80+N*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[N%4])

s.exitonclick()
           
           
            