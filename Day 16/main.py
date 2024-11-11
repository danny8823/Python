import turtle
import another_module
from turtle import Turtle, Screen
from prettytable import PrettyTable
# print(another_module.another_variable)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# my_screen = Screen()

# print(my_screen.canvheight)
# timmy.right(10)
# timmy.forward(100)
# timmy.left(10)
# timmy.forward(100)
# timmy.right(10)
# timmy.forward(100)
# timmy.forward(100)
# timmy.left(10)
# timmy.forward(200)
# timmy.right(10)
# timmy.forward(200)
# timmy.pos()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column = ("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column = ("Type", ["Electric", "Water", "Fire"])
print(table)


# def add_data():
#     table_on = True

#     while table_on:
#         name = input('What is your name?')
#         age = int(input('What is your age?'))
#         title = input('teacher or student?')

#         table.add_row([name, age, title])

#         print(table)
#         add_more = input('Do you wish to add more data? type "y" or "n".')
#         if add_more == 'y':
#             add_data()
#         else:
#             table_on = False

#     print('Done')
#     print('Final Table')
#     print(table)
