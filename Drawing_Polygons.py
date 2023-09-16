import turtle
import math


turtle.setup(width=800, height=800)
turtle.bgcolor("white")


def draw(n, length):
    """
    First argument is the number of side of the polygon.
    Second argument is the length of one side"""

    angle = 180 - ((180 * (n - 2)) / n)  # Internal angle of the polygon
    x0 = -length / 2 #x coordinate of the origin

    y0 = -((length / 2)*math.cos(((angle / 2)*math.pi)/180)) / (math.sin(((angle / 2)*math.pi)/180)) #y coordinate of the origin
    print(angle, x0, y0)

    t = turtle.Turtle() #Creates an instance of class "Turtle" in the library "turtle"


    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.speed(9)
    t.color("red")

    t.begin_fill()
    for x in range(n):

        t.forward(length)
        t.left(angle)

    t.end_fill()
    t.hideturtle()
    turtle.done()

draw(6, 200) #(You might enter(100, 10) for Japanese Flag look)



