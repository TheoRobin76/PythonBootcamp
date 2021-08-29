from turtle import Screen
import time
from snake import Snake, Food, Scoreboard


def play_snake():
    # create the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    # create the starting snake body
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # controlling the snake with the keys
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # moving the snake
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    play_again = True
    while play_again:
        again = screen.textinput(title="Play again?", prompt=f"Would you like to play again? (y/n): ").lower()
        if again == "y":
            screen.clear()
            play_snake()
        elif again == "n":
            play_again = False
            scoreboard.end_game()

    screen.exitonclick()


play_snake()
