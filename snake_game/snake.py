from turtle import Turtle  # Import Turtle class from turtle module

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for snake segments
MOVE_DISTANCE = 20  # Distance to move each snake segment
UP = 90  # Turtle heading direction constants
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class represents the player-controlled snake in the game."""

    def __init__(self):
        """Initialize the snake with starting segments and set the head."""
        self.segments = []  # List to hold snake segments
        self.create_snake()  # Create the initial snake segments
        self.head = self.segments[0]  # Set the head of the snake

    def create_snake(self):
        """Create the initial snake with segments at predefined positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        new_segment = Turtle("square")  # Create a new Turtle segment
        new_segment.color("white")  # Set color of the segment
        new_segment.penup()  # Lift the pen to avoid drawing lines
        new_segment.goto(position)  # Move segment to the specified position
        self.segments.append(new_segment)  # Add segment to the snake's segments list

    def extend(self):
        """Add a new segment to the snake's tail."""
        self.add_segment(self.segments[-1].position())  # Add segment at current tail position

    def move(self):
        """Move the snake forward by updating each segment's position."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get x-coordinate of previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get y-coordinate of previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move current segment to previous segment's position
        self.head.forward(MOVE_DISTANCE)  # Move the head segment forward by MOVE_DISTANCE

    def up(self):
        """Change snake's direction to up (90 degrees) unless currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change snake's direction to down (270 degrees) unless currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change snake's direction to left (180 degrees) unless currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change snake's direction to right (0 degrees) unless currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
