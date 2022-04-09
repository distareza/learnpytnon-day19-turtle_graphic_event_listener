"""
Challenge Create an etch a sketch program that listen to follows key pressed and draw it
w : forward
s : backward
a : counter clockwise ( left )
d : clockwise ( right )
c : clear draw
"""
import turtle
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
pen.hideturtle()

step = 10

def move_forwad():
    turtle.forward(step)
def move_backward():
    turtle.backward(step)
def move_right():
    turtle.right(step)
def move_left():
    turtle.left(step)
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkeypress(move_forwad, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")
screen.onkeypress(clear, "c")

screen.exitonclick()