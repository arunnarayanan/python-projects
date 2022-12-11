import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DIRECTIONS = {'east': 0, 'north': 90, 'west': 180, 'south': 270}

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = t.Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.segments[0].fd(20)

    def up(self):
        if self.head.heading() != DIRECTIONS['south']:
            self.head.seth(DIRECTIONS['north'])

    def down(self):
        if self.head.heading() != DIRECTIONS['north']:
            self.head.seth(DIRECTIONS['south'])

    def left(self):
        if self.head.heading() != DIRECTIONS['east']:
            self.head.seth(DIRECTIONS['west'])

    def right(self):
        if self.head.heading() != DIRECTIONS['west']:
            self.head.seth(DIRECTIONS['east'])