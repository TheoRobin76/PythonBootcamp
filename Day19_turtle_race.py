from turtle import Turtle, Screen
import random

tim = Turtle()
screen1 = Screen() 


# Etch a Sketch
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def counter_clockwise():
#     tim.left(10)
#
#
# def clockwise():
#     tim.right(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen1.listen()
# screen1.onkeypress(key="w", fun=move_forwards)
# screen1.onkeypress(key="s", fun=move_backwards)
# screen1.onkeypress(key="a", fun=counter_clockwise)
# screen1.onkeypress(key="d", fun=clockwise)
# screen1.onkeypress(key="c", fun=clear)
# screen1.exitonclick()


# Turtle Race
is_race_on = False
screen2 = Screen()
screen2.setup(width=500, height=400)
user_bet = screen2.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
for i in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 240:
            winning_color = turtle.pencolor()
            is_race_on = False
            screen2.clear()
            if winning_color == user_bet:
                print(f"You have won, the {winning_color} turtle was victorious!")
            else:
                print(f"You have lost, the {winning_color} turtle was victorious!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
