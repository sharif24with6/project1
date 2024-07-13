# main.py

from turtle import Screen
from snake import Snake
from food import Food
from collision import CollisionManager
from score import Score

# Constants
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off screen updates

# Create snake, food, score, and collision manager
snake = Snake()
food = Food()
score = Score()
collision_manager = CollisionManager(snake, food, screen, score)

# Listen to key events to control the snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

# Define the game loop function
def game_loop():
    if score.is_game_on:
        screen.update()  # Update screen
        snake.move()     # Move snake

        # Check collisions and handle game over
        collision_manager.check_collision()

        # Schedule the next game loop iteration
        screen.ontimer(game_loop, 100)  # Adjust delay here (100 milliseconds)
    else:
        # Game over handling
        play_again = screen.textinput("Game Over", "Do you want to play again? (yes/no)").lower()
        if play_again == "yes":
            score.reset()
            snake.reset()
            screen.update()
            score.is_game_on = True
            game_loop()

# Start the game loop
game_loop()

# Exit the game on click
screen.exitonclick()
