import turtle as x1
x1.bgcolor('black')
x1.pensize(1)
x1.speed(10)
for i in range(6):
    for color in ('#2343de', '#592F2F', '#e95F20', 
                  '#ac2e2F', '#72db28', '#1cda79',
                  '#ab3Fa1'):
        x1.color(color)
        x1.circle(100)
        x1.left(10)
    x1.hideturtle()
x1.exitonclick()
