import turtle
import random

window = turtle.Screen()
window.bgcolor("purple")

n = random.random()

turtle = turtle.Turtle()
turtle.speed(3000)

turtle.forward(-350 )

def drowSquare():
    for i in range(1, 5):
        turtle.forward(50 )
        turtle.right(90 )


def turnLestAndDrow():
    for i in range(1, 37):
        turtle.left(10)
        drowSquare()

# def drowFlower():
#     for i in range(1, 2):
#         turnLestAndDrow()
#         turtle.forward(512 + n)
#         turtle.left(180 + n)

def sushen():
    def s():
        turtle.forward(-80)
        turtle.left(-90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(80)
        turtle.left(-90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(-80)
        turtle.forward(90)

    def u():
        turtle.left(90)
        turtle.forward(60)
        turtle.left(180)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(180)
        turtle.forward(60)

    s()
    u()
    # S
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(-90)
    turtle.forward(60)
    turtle.left(-90)
    turtle.forward(80)

    # Riverse S
    turtle.left(180)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(-90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(10)

    #h
    turtle.left(90)
    turtle.forward(120)
    turtle.left(180)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(-90)
    turtle.forward(60)

    #e
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(-90)
    turtle.forward(60)
    turtle.left(-90)
    turtle.forward(30)
    turtle.left(-90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(70)

    #n
    turtle.left(90)
    turtle.forward(60)
    turtle.left(-90)
    turtle.forward(60)
    turtle.left(-90)
    turtle.forward(60)

turnLestAndDrow()
turtle.left(0)
turtle.forward(250)
sushen()
turtle.left(0)
turtle.forward(50)
turnLestAndDrow()


window.exitonclick()
