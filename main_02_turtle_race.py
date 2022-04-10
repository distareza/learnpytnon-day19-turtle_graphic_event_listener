"""
Challenges create a guess who ran faster
"""
import random
from turtle import Turtle, Screen

screen_width = 500
screen_height = 400
distance_size = 30
start_line = (distance_size - screen_width) / 2
finish_line = (screen_width / 2) - distance_size
screen = Screen()
screen.setup(width=screen_width, height=screen_height)

colors = ["red", "yellow", "blue", "purple", "orange", "green", "violet", "indigo"]
user_bet = ""
while True:
    user_bet = screen.textinput("Make your bet", f"Which turtle is win the race ? {colors}")
    if user_bet in colors:
        break

contestant = []

top_position = (len(colors) * distance_size / 2)

for color in colors:
    turtle = Turtle(shape="turtle")
    contestant += [turtle]
    turtle.color(color)
    turtle.penup()
    turtle.goto(start_line, top_position)
    top_position -= distance_size


winner = {}
while not winner:
    for turtle in contestant:
        turtle.forward(random.randint(0, 10))
        position = turtle.xcor()
        if position > finish_line:
            winner = turtle
            break

print(f"the winner is {winner.pencolor()}")
if user_bet == winner.pencolor():
    print("You Win!")
else:
    print("Sorry, You Lose")

screen.exitonclick()
