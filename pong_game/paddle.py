from turtle import Turtle

class Paddle(Turtle):
    """
    A paddle for a game.
    """

    def __init__(self, position):
        """
        Initialize paddle attributes and position.
        """
        super().__init__()
        self.shape("square")    # Set paddle shape
        self.color("white")     # Set paddle color
        self.shapesize(5, 1)    # Set paddle size
        self.penup()            # Lift pen to move without drawing
        self.goto(position)     # Move paddle to starting position

    def move_up(self):
        """
        Move paddle up by 20 units.
        """
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        """
        Move paddle down by 20 units.
        """
        self.goto(self.xcor(), self.ycor() - 20)
