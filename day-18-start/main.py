from turtle import Turtle, Screen
import random


tim = Turtle()
# tim.shape("turtle")
tim.color("red")

colors = ["Red", "Dark", "Blue", "Green", "Yellow", "Orange", "Violet", "Pink", "Purple"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_number in range(3, 11):
    draw_shape(shape_side_number)
    tim.color(random.choice(colors))

screen = Screen()
screen.exitonclick()