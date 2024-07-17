from turtle import Turtle  # Import Turtle class from turtle module

ALIGNMENT = "center"  # Constant for text alignment
FONT = ("Courier", 24, "normal")  # Constant for text font

class Scoreboard(Turtle):
    """Scoreboard class manages displaying and updating the game score."""

    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()  # Initialize the Turtle base class
        self.score = 0  # Initialize score to zero
        self.color("white")  # Set text color to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 270)  # Position the scoreboard at the top center
        self.hideturtle()  # Hide the turtle icon
        self.update_scoreboard()  # Display initial score

    def update_scoreboard(self):
        """Update the scoreboard with the current score."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display 'GAME OVER' message."""
        self.goto(0, 0)  # Position the cursor to the center
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Write 'GAME OVER'

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1  # Increment the score
        self.clear()  # Clear previous score display
        self.update_scoreboard()  # Update scoreboard with new score
