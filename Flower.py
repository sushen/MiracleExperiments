import turtle
import random

window = turtle.Screen()
window.bgcolor("yellow")

n = random.random()

turtle = turtle.Turtle()
turtle.speed(3000 + n)


def drowSquare():
    for i in range(1, 5):
        turtle.forward(50 + n)
        turtle.right(90 + n)


def turnLestAndDrow():
    for i in range(1, 37):
        turtle.left(10 + n)
        drowSquare()

def drowFlower():
    for i in range(1, 20):
        turnLestAndDrow()
        turtle.forward(150 + n)
        turtle.left(70 + n)

drowFlower()

window.exitonclick()
