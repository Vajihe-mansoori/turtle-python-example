import turtle
colors=['#13eacc','#10aaff','#2352ee']
draw=turtle.Pen()
turtle.bgcolor('black')
draw.speed(100)

for a in range(360):
    draw.pencolor(colors[a%3])
    draw.width(1)
    draw.forward(a)
    draw.left(100)

turtle.done()