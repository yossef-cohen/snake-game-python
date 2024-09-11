from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # initialize the list that the snake going to be saved
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    # create the starting snake
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # add a segment to the snake after food was consumed
    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.turtle_list.append(t)

    # reset the snake to the start when lost
    def reset(self):
        for turtles in self.turtle_list:
            turtles.goto(10000, 10000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    # define the location of the segment
    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    # the movement of the segments
    def move(self):
        for seg in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[seg - 1].xcor()
            new_y = self.turtle_list[seg - 1].ycor()
            self.turtle_list[seg].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    # the movement of the snake when a key is pressed
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
