import turtle

turtle.speed(30)
sidelength = 35
point = 6
side2 = 2


def octagon(side):
    for size in range(8):
        turtle.left(70)
        turtle.forward(side)

def pentagon(sidelength):
    for size in range(5):
        turtle.right(45)
        turtle.forward(sidelength)

def circle(point):
    for size in range(30):
        turtle.left(10)
        turtle.right(point)
        turtle.forward(5)

def square(side2):
    for size in range(4):
        turtle.forward(50)
        turtle.right(90)

for size in range(95):
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    octagon(size)
    turtle.right(5)
    turtle.color("gray")
    turtle.forward(20)
    turtle.backward(70)
    circle(point)
    turtle.right(80)
    turtle.forward(5)

for size in range(70):
    turtle.penup()
    turtle.goto(200, 350)
    turtle.pendown()
    turtle.forward(80)
    pentagon(sidelength)
    turtle.right(20)
    turtle.forward(10)
    square(side2)
    turtle.left(10)
    turtle.forward(3)

for size in range(70):
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    circle(point)
    turtle.right(25)
    turtle.backward(15)
    turtle.forward(5)
    turtle.left(10)
    turtle.forward(3)

for size in range(30):
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()
    square(side2)
    turtle.backward(20)
    turtle.right(45)
    turtle.forward(10)
    turtle.left(10)
    turtle.forward(3)

turtle.exitonclick()