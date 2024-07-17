from turtle import Turtle  # Import Turtle class from turtle module
import random  # Import random module for generating random coordinates


class Food(Turtle):
    """Food class represents the food that the snake eats."""

    def __init__(self):
        """Initialize the food appearance and position."""
        super().__init__()  # Initialize the Turtle base class
        self.shape("circle")  # Set the shape of the food to circle
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Stretch the circle shape
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the animation speed to the fastest possible
        self.refresh()  # Place the food at a random position initially

    def refresh(self):
        """Move the food to a random position within the screen boundaries."""
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the random position
