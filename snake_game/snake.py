from turtle import Turtle

MOVE_DISTANCE = 20  # Adjust as needed
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Assign the first segment as the head

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        # Add a new segment to the snake
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments out of the screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # Reassign the head after reset

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def head_position(self):
        return self.head.position()  # Return current position of the head

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
