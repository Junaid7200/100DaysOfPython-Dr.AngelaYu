# July 6, 2024

# with open("INTERMEDIATE/weather-data.csv") as file:
#     lines = file.readlines()
#     print(lines)


# import csv

# with open("INTERMEDIATE/weather-data.csv") as file:
#     data = csv.reader(file)
#     temps = []
#     for row in data:
#         print(row)
#         temps.append(row[1])
#     temp2 = []
#     for temp in temps[1:]:
#         temp2.append(int(temp))

# print(temp2)

from sre_constants import JUMP
import pandas as pd 
# data = pd.read_csv("INTERMEDIATE/weather-data.csv")
# print(type(data))
# series_data = data["temp"]
# list_data = series_data.to_list()
# print(list_data)
# print(f"avg temp is: { data["temp"].mean():.2f}")
# print(f"max temp is: { data["temp"].max():.2f}")

# print(data[data.day == "Monday"])
# print("max row: ")
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# Mtemp = monday.temp
# print(Mtemp * 9/5 +32)

# data frames VS series in pandas: df is basically the whole table, series is like a list/column of that df

# dict_data = data.to_dict()
# print(dict_data)

# data = pd.read_csv("INTERMEDIATE/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# gray = data[data["Primary Fur Color"] == "Gray"]
# NoOfGray = len(gray)
# Cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
# NoOfCinnamon = len(Cinnamon)
# Black = data[data["Primary Fur Color"] == "Black"]
# NoOfBlack = len(Black)

# dict =  {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [NoOfGray, NoOfCinnamon, NoOfBlack]
# }
# new_df = pd.DataFrame(dict)
# print(new_df)

# new_df.to_csv("squirrel_count.csv")



# 50 states
import turtle as t 
screen = t.Screen()
screen.setup(width=750, height=700)
screen.title("U.S states Game")

image = "INTERMEDIATE/blank_states_img.gif"
screen.addshape(image)
t.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)

t.onscreenclick(get_mouse_click_coor)




data = pd.read_csv("INTERMEDIATE/50_states.csv")

states = data["state"].to_list()

game_on = True
while game_on:
    answer_state = screen.textinput(title= "Guess a State", prompt="Write a state name").title()
    if answer_state == "Exit":
        game_on = False
        break
    for state in states:
        if state == answer_state:
            row = data[data["state"] == answer_state]
            print(row)
            x_cor = row["x"].values[0]
            y_cor = row["y"].values[0]
            print(x_cor)
            print(y_cor)
            new_t = t.Turtle()
            new_t.penup()
            new_t.hideturtle()
            new_t.goto(x = x_cor, y = y_cor)
            new_t.write(f"{answer_state}", align="center")


if game_on:
    t.mainloop()            





