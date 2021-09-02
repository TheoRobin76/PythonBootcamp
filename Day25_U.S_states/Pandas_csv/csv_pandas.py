# with open("weather_data.csv.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
# print(data["condition"])
# print(data.condition)

# get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * (9/5) + 32
# print(monday_temp_F)
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Theo", "Brian", "Mandy"],
#     "scores": [76, 11, 92]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"]
red = len(data[fur_data == "Cinnamon"])
grey = len(data[fur_data == "Gray"])
black = len(data[fur_data == "Black"])

# print(f"Cinnamon count: {red}")
# print(f"Gray count: {grey}")
# print(f"Black count: {black}")

squirrel_dict = {
    "Fur color": ["Grey", "Red", "Black"],
    "Count": [grey, red, black]
}

squirrel_data = pandas.DataFrame(squirrel_dict)
squirrel_data.to_csv("squirrel_count.csv")
print(squirrel_data)
