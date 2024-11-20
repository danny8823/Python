import random
import pandas
# numbers = [1, 2, 3]


# def new_item(n):
#     return n + 1


# new_numbers = [n + 1 for n in numbers]

# name = "Angela"

# new_list = [letter for letter in name]

# double_numbers = [n * 2 for n in range(1, 5)]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']


# short_names = [name.upper() for name in names if len(name) > 5]


# print(short_names)

# missing_states = [states for states not in ]

# student_scores = {student: random.randint(1, 100) for student in names}

# passed_students = {student: student_scores[student]
#                    for student in student_scores if student_scores[student] > 70}

# passed_students_2 = {student: score for (
#     student, score) in student_scores.items() if score > 60}
# print('scores', student_scores)
# print(passed_students_2)
# print(student_scores.items())

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
