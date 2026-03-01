from turtle import Turtle, Screen
import random

is_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


def draw_finish_line():
    line_turtle = Turtle()
    line_turtle.hideturtle()
    line_turtle.penup()
    line_turtle.speed("fastest")
    line_turtle.goto(x=210, y=120)
    line_turtle.right(90)
    line_turtle.pendown()
    line_turtle.forward(220)


draw_finish_line()

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle wins.")
            else:
                print(f"You lose! The {winning_color} turtle wins.")
            break

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
