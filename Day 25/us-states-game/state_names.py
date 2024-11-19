from turtle import Turtle
FONT = ("Courier", 12, "normal")


class State_Names(Turtle):
    def __init__(self):
        super().__init__()

    def write_state(answer, x, y):
        print(answer, x, y)
        pen = Turtle()
        pen.penup()
        pen.hideturtle()
        pen.color('black')
        pen.goto(x, y)
        pen.write(f'{answer}', align='center', font=FONT)
