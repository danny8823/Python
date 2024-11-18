from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 25, 'normal')

score_data = open(
    "/Users/danny714/Desktop/Python/Day 24/data.txt", "r", encoding="utf-8")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color('white')
        self.score = 0
        self.high_score = int(score_data.read())
        self.hideturtle()
        self.goto(0, 260)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {
                   self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open(
                "/Users/danny714/Desktop/Python/Day 24/data.txt", "w", encoding="utf-8")

            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
