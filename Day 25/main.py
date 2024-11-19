import csv
import pandas

f = open("/Users/danny714/Desktop/Python/Day 25/weather_data.csv")

# with f as data_file:
#     data = data_file.readlines()
#     print(data)

with f as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))

weather_data = pandas.read_csv(
    "/Users/danny714/Desktop/Python/Day 25/weather_data.csv")

data_dict = weather_data.to_dict()

temp_list = weather_data['temp'].to_list()

temp_data = weather_data["temp"]

temp = weather_data['temp']
max_temp = temp.max()
max_temp_row = weather_data[weather_data.temp == max_temp]

monday = weather_data[weather_data.day == "Monday"]
monday_temp = monday.temp[0]

monday_temp_f = monday_temp * 9/5 + 32

# Create a datafram from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(data_dict)
student_data.to_csv(
    "/Users/danny714/Desktop/Python/Day 25/student_data.csv")
print(student_data)
