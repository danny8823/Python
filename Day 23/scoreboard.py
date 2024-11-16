from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f'Level: {self.level}', align="center", font=FONT)

    def up_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color('black')
        self.hideturtle()
        self.write(f'Game Over', align='center', font=FONT)
