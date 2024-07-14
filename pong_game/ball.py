from turtle import Turtle

class Ball(Turtle):
    """
    A class representing a ball in a game.
    """

    def __init__(self):
        """
        Initialize the ball's attributes.
        """
        super().__init__()       # Initialize the Turtle base class
        self.shape("circle")     # Set ball shape to circle
        self.color("white")      # Set ball color to white
        self.penup()             # Lift pen to move without drawing lines
        self.x_move = 10         # Initial movement speed in x-direction
        self.y_move = 10         # Initial movement speed in y-direction
        self.move_speed = 0.1    # Initial movement speed factor

    def move(self):
        """
        Move the ball based on its current x_move and y_move speeds.
        """
        new_x = self.xcor() + self.x_move   # Calculate new x-coordinate
        new_y = self.ycor() + self.y_move   # Calculate new y-coordinate
        self.goto(new_x, new_y)             # Move the ball to the new coordinates

    def bounce_y(self):
        """
        Reverse the y-direction of the ball and decrease its movement speed.
        """
        self.y_move *= -1        # Reverse y-direction
        self.move_speed *= 0.9   # Decrease movement speed

    def bounce_x(self):
        """
        Reverse the x-direction of the ball and decrease its movement speed.
        """
        self.x_move *= -1        # Reverse x-direction
        self.move_speed *= 0.9   # Decrease movement speed

    def reset_position(self):
        """
        Reset the ball's position to the center of the screen and reset its movement.
        """
        self.goto(0, 0)          # Move ball to center
        self.bounce_x()          # Reset x-direction
        self.move_speed = 0.1    # Reset movement speed
