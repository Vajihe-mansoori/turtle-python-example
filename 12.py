import turtle 
colors=['#ff2132','#971190','#1fffff','#119421','#d4e256','#74213b'] 
turtle.bgcolor('black') 
turtle.speed(10)
turtle.pensize(1)
for x in range(360): 
    turtle.pencolor(colors[x%6]) 
    turtle.width(x/100+1) 
    turtle.forward(x) 
    turtle.left(59)

turtle.exitonclick()