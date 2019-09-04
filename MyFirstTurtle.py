import turtle

turtle.shape("turtle")

numOfSides = 19
angle = 360/numOfSides

x = 0
y = 0

loadWindow = turtle.Screen()
turtle.speed(6)

turtle.speed(20)
side = 100
t = turtle.Turtle()

for i in range(3):
    for i in range(3):
        turtle.color("red")
        turtle.left(angle)
        turtle.forward(45)
        turtle.right(angle)
        turtle.forward(30)

    for i in range(5):
        turtle.color("orange")
        turtle.forward(40)
        turtle.left(110)

    for i in range(numOfSides):
        turtle.color("gold")
        turtle.forward(50)
        turtle.right(45)
        turtle.left(angle)

    for i in range(15):
        turtle.color("blue")
        turtle.forward(25)
        turtle.right(20)
        turtle.forward(10)
        turtle.left(25)
        turtle.forward(55)
        turtle.right(25)
        turtle.backward(45)

        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()

        turtle.left(10)

    for i in range(25):
        turtle.color("black")
        turtle.right(angle)
        turtle.forward(50)
        turtle.left(45)
        turtle.forward(60)
        turtle.backward(75)
        turtle.right(90)
        turtle.forward(30)
        turtle.backward(40)
        turtle.left(90)
        turtle.forward(40)
        turtle.right(45)
        turtle.forward(40)
        turtle.left(45)
    for i in range(25):
        turtle.color("aquamarine")
        turtle.right(angle)
        turtle.backward(10)
        turtle.left(-15)
        turtle.color("black")
        turtle.backward(20)
        turtle.forward(30)
        turtle.color("yellow")
        turtle.left(40)
        turtle.forward(-50)
        turtle.color("pink")
        turtle.backward(60)
        turtle.right(-70)
        turtle.color("green")
        turtle.forward(80)
        turtle.right(90)
        turtle.color("brown")
        turtle.forward(100)
        turtle.left(-20)
    for i in range(25):
        turtle.color("black")
        turtle.left(angle)
        turtle.forward(32)
        turtle.left(9)
        turtle.backward(35)
        turtle.forward(32)
        turtle.left(26)
        turtle.forward(8)
        turtle.backward(10)
        turtle.color("dark red")
        turtle.left(90)
        turtle.forward(21)
        turtle.left(9)
        turtle.backward(14)
        turtle.left(10)
    for i in range(70):
        turtle.color("green")
        turtle.forward(50)
        turtle.right(15)
        turtle.forward(10)
        turtle.left(25)

        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()

        turtle.right(4)
    for i in range(60):
        turtle.color("gray")
        turtle.circle(2*i)
        turtle.circle(-2*i)
        turtle.right(i)
    for i in range(50):
        turtle.color("purple")
        turtle.forward(100)
        turtle.left(72)
    for i in range(30):
        turtle.color("gold")
        turtle.forward(i * 20)
        turtle.right(45)
    for i in range(75):
        t.color("red")
        t.backward(side)
        t.right(45)
        side = side - 10

turtle.color("pink")
turtle.exitonclick()