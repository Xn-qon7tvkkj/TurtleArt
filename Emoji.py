import turtle
import square

scn = turtle.Screen()
no = turtle.Turtle()
ko = turtle.Turtle()
se = turtle.Turtle()
que = turtle.Turtle()


def circle(side):
    for size in range(42):
        no.forward(70)
        no.right(10)


def circle3(side):
    for size in range(65):
        que.forward(8)
        que.left(6)


def circle4(side):
    for size in range(65):
        que.forward(8)
        que.left(6)

def circle5(side):
    for size in range(65):
        se.forward(1)
        se.left(6)

def eye1(side):
    for size in range(65):
        ko.forward(8)
        ko.left(6)


def eye2(side):
    for size in range(65):
        se.forward(8)
        se.left(6)


def mouth(side):
    for size in range(35):
        que.forward(4)
        que.left(3)


def eye3(side):
    for size in range(60):
        no.forward(4)
        no.left(6)


def eye4(side):
    for size in range(60):
        ko.forward(4)
        ko.left(6)


scn.bgcolor("black")

no.fillcolor("yellow")
no.penup()
no.goto(0, 300)
no.pendown()
no.pencolor("yellow")
no.begin_fill()
circle(1)
no.end_fill()

ko.fillcolor("white")
ko.penup()
ko.goto(-50, 0)
ko.pendown()
ko.pencolor("white")
ko.begin_fill()
eye1(1)
ko.end_fill()

se.fillcolor("white")
se.penup()
se.goto(-50, -200)
se.pendown()
se.pencolor("white")
se.begin_fill()
eye2(1)
se.end_fill()

que.fillcolor("brown")
que.penup()
que.goto(200, -150)
que.pendown()
que.pencolor("brown")
que.begin_fill()
que.forward(70)
que.left(90)
que.forward(150)
que.left(90)
que.forward(70)
que.left(90)
que.forward(150)
que.left(90)
que.end_fill()

no.fillcolor("black")
no.penup()
no.goto(-118, 70)
no.pendown()
no.pencolor("black")
no.begin_fill()
eye3(1)
no.end_fill()

ko.fillcolor("black")
ko.penup()
ko.goto(-68, -150)
ko.pendown()
ko.pencolor("black")
ko.begin_fill()
eye4(1)
ko.end_fill()

que.fillcolor("pink")
que.penup()
que.goto(155, -330)
que.pendown()
que.pencolor("pink")
que.begin_fill()
circle3(1)
que.end_fill()

que.fillcolor("pink")
que.penup()
que.goto(170, 100)
que.pendown()
que.pencolor("pink")
que.begin_fill()
circle4(1)
que.end_fill()

se.fillcolor("white")
se.penup()
se.goto(-87, 70)
se.pendown()
se.pencolor("white")
se.begin_fill()
circle5(1)
se.end_fill()

se.fillcolor("white")
se.penup()
se.goto(-87, -130)
se.pendown()
se.pencolor("white")
se.begin_fill()
circle5(1)
se.end_fill()

scn.exitonclick()
