import time
from turtle import Turtle,Screen
from actual_snake import Snake
from food import Food
from scoreboard import Score_board
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake=Snake()
snake.create()
food=Food()
score_board=Score_board()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snakes[0].distance(food) < 15:
        score_board.increase_score()
        food.set_color()
        food.refresh()
        snake.extend()

    if snake.snakes[0].xcor()>280 or snake.snakes[0].xcor()<-280 or snake.snakes[0].ycor()<-280 or snake.snakes[0].ycor()>280:
        snake.reset()
        score_board.game_over()


    for segment in snake.snakes[1:]:
            if snake.snakes[0].distance(segment)<10:
                snake.reset()
                score_board.game_over()


screen.exitonclick()