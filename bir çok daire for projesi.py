import turtle
turtle.pensize(3)
turtle.bgcolor("grey")
turtle.pencolor("blue")

for x in range(36):
    turtle.home()
    turtle.left(x*10)
    turtle.circle(100)
