import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. State Game")

# Add the image of the blank U.S. map
image = "blank_states_img.gif"  
screen.addshape(image)
turtle.shape(image)

# Read the CSV data with state names and their coordinates
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    # Prompt the user to enter a state name
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Exit the game if the user types 'Exit'
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")  # Save the missing states to a CSV file
        break

    # Check if the entered state is correct
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Exit on click
screen.exitonclick()
