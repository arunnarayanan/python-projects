from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score.txt', 'r') as score_file:
            score_from_file = score_file.read()
            self.high_score = int(score_from_file)
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score = 0 \t High Score = {self.high_score}', align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', 'w') as score_file:
                score_file.write(str(self.high_score))

        self.write(f'Score = {self.score} \t High Score = {self.high_score}', align='center', font=('Arial', 24, 'normal'))
