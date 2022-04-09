"""
    Turtle Graphic Order Function and Event Listener
"""

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


screen.onkey(key="space", fun=move_forward)
screen.listen()

screen.exitonclick()