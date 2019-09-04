import turtle

turtle.speed(30)

sidelength = 100

def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)

for i in range(60):
        square(sidelength)
        turtle.right(5)

turtle.exitonclick()
