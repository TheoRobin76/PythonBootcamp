import time
from turtle import Screen
from turtle_crossing import CarManager, Player, Scoreboard, FINISH_LINE_Y

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# instantiate the classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# keyboard input for the turtle
screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create and move the cars
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect when turtle reaches the next level
    if player.ycor() > FINISH_LINE_Y:
        player.next_level()
        car_manager.level_up()
        scoreboard.new_level()

screen.exitonclick()