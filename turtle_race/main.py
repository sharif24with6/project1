from turtle import Turtle, Screen
import random
import time

# Function to clear previous race setup and prepare for a new race
def reset_race():
    screen.clear()  # Clear the screen
    all_turtles.clear()  # Clear the list of turtles
    # Create 6 new turtles with random speeds and positions
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])  # Set turtle color
        new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Set turtle starting position
        new_turtle.speed(random.randint(1, 10))  # Set random speed for each turtle
        all_turtles.append(new_turtle)  # Add turtle to the list of all turtles

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)

# Define available turtle colors and their starting positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Initialize an empty list to store all turtle objects
all_turtles = []

# Call reset_race function to setup initial race
reset_race()

# Prompt user to input their bet on which turtle will win
user_bet = None
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Choose from {', '.join(colors)}: ").lower()

# Flag to control the race loop
is_race_on = True

# Main race loop
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)  # Generate random distance for turtle to move
        turtle.forward(rand_distance)  # Move turtle forward by rand_distance pixels

        # Check if turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False  # End race loop
            winning_color = turtle.pencolor().lower()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")  # Print win message if user's bet matches winning turtle
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")  # Print lose message if user's bet does not match winning turtle

            time.sleep(1)  # Pause for 1 second before asking user for restart

            # Ask user if they want to race again
            restart = screen.textinput(title="Race Over", prompt="Do you want to race again? Type 'yes' or 'no': ").lower()
            if restart == 'yes':
                is_race_on = True  # Restart the race
                reset_race()  # Call reset_race function to setup new race
            else:
                is_race_on = False  # End the program if user does not want to race again

# Close the turtle graphics window
screen.bye()
