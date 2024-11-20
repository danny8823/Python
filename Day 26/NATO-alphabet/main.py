import pandas
import os
import random

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    value[0]
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    row.student
    row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_alphabet_csv = open(
    "/Users/danny714/Desktop/Python/Day 26/NATO-alphabet/nato_phonetic_alphabet.csv")

nato_abc_data = pandas.read_csv(nato_alphabet_csv)

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_abc_dict = {row.letter: row.code for (
    index, row) in nato_abc_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input_letters = []
user_input = input(
    'Write a word to translate into nato phonetic_alphabet.').upper()

output_list = [nato_abc_dict[letter] for letter in user_input]

print(output_list)
