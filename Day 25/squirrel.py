import csv
import pandas

data = pandas.read_csv(
    "/Users/danny714/Desktop/Python/Day 25/squirrel_data.csv")


gray_count = 0
red_count = 0
black_count = 0
for color in data['Primary Fur Color']:
    if color == 'Gray':
        gray_count += 1
    elif color == 'Cinnamon':
        red_count += 1
    elif color == 'Black':
        black_count += 1

squirrel_dictionary = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count": [gray_count, red_count, black_count]
}

squirrel_count = pandas.DataFrame(squirrel_dictionary)
squirrel_count.to_csv(
    "/Users/danny714/Desktop/Python/Day 25/squirrel_count.csv")
