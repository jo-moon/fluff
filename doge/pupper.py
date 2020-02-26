import turtle
import time

def draw_square():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

def draw(colour):
    turtle.color(colour)
    for i in range(360):
        draw_square()
        turtle.left(i)
