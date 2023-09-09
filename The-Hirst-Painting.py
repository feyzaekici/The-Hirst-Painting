import turtle as t
import random

a = t.Turtle()
screen = t.Screen()

a.hideturtle()
a.penup()
a.speed('fastest')
t.colormode(255)
color_list = [(226, 231, 235), (52, 93, 124), (225, 201, 108), (134, 85, 58), (229, 235, 234), (172, 154, 40)]

a.setheading(225)
a.forward(300)
a.setheading(0)

for x in range(1, 101):
    a.dot(20, random.choice(color_list))
    a.forward(50)

    if x % 10 == 0:
        a.setheading(90)
        a.forward(50)
        a.setheading(180)
        a.forward(500)
        a.setheading(0)

screen.exitonclick()