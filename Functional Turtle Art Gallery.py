import turtle


sidelength = 35
point = 6
side2 = 2

ral = turtle.Turtle()
ral.speed('fastest')


def octagon(side):
    for size in range(8):
        ral.left(70)
        ral.forward(side)

def pentagon(sidelength):
    for size in range(5):
        ral.right(45)
        ral.forward(sidelength)

def circle(point):
    for size in range(30):
        ral.left(10)
        ral.right(point)
        ral.forward(5)

def square(side2):
    for size in range(4):
        ral.forward(50)
        ral.right(90)

for size in range(95):
    ral.penup()
    ral.goto(-200, 200)
    ral.pendown()
    octagon(size)
    ral.right(5)
    ral.color("gray")
    ral.forward(20)
    ral.backward(70)
    circle(point)
    ral.right(80)
    ral.forward(5)

for size in range(70):
    ral.penup()
    ral.goto(200, 350)
    ral.pendown()
    ral.forward(80)
    pentagon(sidelength)
    ral.right(20)
    ral.forward(10)
    square(side2)
    ral.left(10)
    ral.forward(3)

for size in range(70):
    ral.penup()
    ral.goto(0, -300)
    ral.pendown()
    circle(point)
    ral.right(25)
    ral.backward(15)
    ral.forward(5)
    ral.left(10)
    ral.forward(3)

for size in range(30):
    ral.penup()
    ral.goto(100, 100)
    ral.pendown()
    square(side2)
    ral.backward(20)
    ral.right(45)
    ral.forward(10)
    ral.left(10)
    ral.forward(3)


ral.exitonclick()