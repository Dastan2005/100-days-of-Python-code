import turtle
import pandas
# # import csv
# # # with open("weather_data.csv") as data:
# # #     data = data.readlines()
# # #     print(data)
# #
# # with open("weather_data.csv") as data:
# #     data = csv.reader(data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #         print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # temp_list = data["temp"].to_list()
# # # average = sum(temp_list) / len(temp_list)
# # # print(average)
# # # print(data["temp"].mean())
# # print(data["temp"].max())
# monday = data[data["day"] == "Monday"]
# mon_temp = monday.temp[0]
# fahrenheit = ((9 / 5) * mon_temp) + 32
# print(fahrenheit)

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

states_to_learn = all_states - guessed_states
