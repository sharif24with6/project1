#still game in devlopment
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)  # Turn off automatic screen updates

# Create paddles, ball, and score objects
r_paddle = Paddle((350, 0))  # Create a paddle on the right side
l_paddle = Paddle((-350, 0))  # Create a paddle on the left side
ball = Ball()  # Create the game ball
score = Score()  # Create the score display

# Set up keyboard input
screen.listen()
screen.onkey(r_paddle.move_up, "Up")    # Right paddle moves up on "Up" key press
screen.onkey(r_paddle.move_down, "Down")  # Right paddle moves down on "Down" key press
screen.onkey(l_paddle.move_up, "w")      # Left paddle moves up on "w" key press
screen.onkey(l_paddle.move_down, "s")    # Left paddle moves down on "s" key press

game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(ball.move_speed)  # Pause to control ball speed
    screen.update()  # Update the screen manually

    ball.move()  # Move the ball

    # Check if the ball hits the top or bottom walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check if the ball collides with paddles and bounce
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Check if the ball goes out of bounds on the right side
    if ball.xcor() > 380:
        ball.reset_position()  # Reset ball position
        score.l_point()  # Increase left player's score

    # Check if the ball goes out of bounds on the left side
    if ball.xcor() < -380:
        ball.reset_position()  # Reset ball position
        score.r_point()  # Increase right player's score

# Exit the game when clicking on the screen
screen.exitonclick()
