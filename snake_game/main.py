# Import necessary modules and classes
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off screen updates

# Create snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update screen after each iteration
    time.sleep(0.1)  # Introduce a small delay for smoother gameplay
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh food position
        snake.extend()  # Extend snake length
        scoreboard.increase_score()  # Increase score

    # Detect collision with walls
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()  # Display game over message

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Check collision with all segments except the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()  # Display game over message

# Keep the window open until clicked
screen.exitonclick()
