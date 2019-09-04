import turtle

turtle.speed(30)


def star(side):
    for size in range(5):
        turtle.left(144)
        turtle.forward(side)

for size in range(95):
    star(size)
    turtle.right(5)

for size in range(72):
    turtle.penup()
    turtle.goto(100, 200)
    turtle.pendown()
    star(size)
    turtle.right(5)

for size in range(75):
    turtle.penup()
    turtle.goto(100, -200)
    turtle.pendown()
    star(size)
    turtle.right(5)


for size in range(70):
    turtle.penup()
    turtle.goto(300, 100)
    turtle.pendown()
    star(size)
    turtle.right(5)


turtle.exitonclick()