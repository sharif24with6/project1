from turtle import Screen
from snake import Snake
from food import Food
from score import Score

class CollisionManager:
    def __init__(self, snake: Snake, food: Food, screen: Screen, score: Score):
        self.snake = snake
        self.food = food
        self.screen = screen
        self.score = score

    def check_collision(self):
        # Check if snake collides with food
        if self.snake.head.distance(self.food) < 15:
            self.food.refresh()
            self.snake.extend()
            self.score.increase_score()

        # Check if snake collides with wall
        if abs(self.snake.head.xcor()) > 290 or abs(self.snake.head.ycor()) > 290:
            self.score.game_over()
            self.score.is_game_on = False

        # Check if snake collides with itself
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < 10:
                self.score.game_over()
                self.score.is_game_on = False
