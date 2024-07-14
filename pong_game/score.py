from turtle import Turtle

class Score(Turtle):
    """
    A class representing the score display for a game.
    """

    def __init__(self):
        """
        Initializes the score display attributes.
        """
        super().__init__()      # Initialize the Turtle base class
        self.color("white")     # Set text color to white
        self.penup()            # Lift pen to avoid drawing lines
        self.hideturtle()       # Hide the turtle icon
        self.l_score = 0        # Initialize left player's score to 0
        self.r_score = 0        # Initialize right player's score to 0

    def l_point(self):
        """
        Increment the left player's score by 1 and update the display.
        """
        self.l_score += 1       # Increment left player's score
        self.update_score()     # Update the score display

    def r_point(self):
        """
        Increment the right player's score by 1 and update the display.
        """
        self.r_score += 1       # Increment right player's score
        self.update_score()     # Update the score display

    def update_score(self):
        """
        Clear the old score and write the updated scores at their respective positions.
        """
        self.clear()                                  # Clear previous score display
        self.goto(-100, 200)                          # Position for left player's score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  # Write left player's score
        self.goto(100, 200)                           # Position for right player's score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  # Write right player's score
