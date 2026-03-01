import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backfards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
turtle.onkey(key="w", fun=move_forwards)
turtle.onkey(key="s", fun=move_backfards)
turtle.onkey(key="a", fun=turn_left)
turtle.onkey(key="d", fun=turn_right)
turtle.onkey(key="c", fun=clear)

screen.exitonclick()
