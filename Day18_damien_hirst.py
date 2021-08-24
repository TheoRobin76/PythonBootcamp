from turtle import Turtle, Screen
import turtle as t
import random
import colorgram

# turtle documentation: https://docs.python.org/3/library/turtle.html
# turtle colours: https://cs111.wellesley.edu/labs/lab01/colors
# more turtle colours: https://trinket.io/docs/colors

tim = Turtle()
tim.shape("turtle")
tim.color("DarkSlateBlue")

# draw a square
for i in range(4):
    tim.forward(100)
    tim.right(90)

# draw a dashed line
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# drawing different shapes
colours = ["indigo", "DarkSlateBlue", "OrangeRed", "LightSeaGreen",
           "CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "SlateGray", "wheat", "orange", "black", "ForestGreen", "green3"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape)


# random walk
t.colormode(255)
angles = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


for i in range(500):
    tim.forward(30)
    tim.setheading(random.choice(angles))
    tim.color(random_colour())


# draw a spirograph
for i in range(72):
    tim.color(random_colour())
    tim.circle(100)
    tim.left(5)

# Damien Hirst spot painting
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126),
              (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75),
              (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (222, 177, 182),
              (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48),
              (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25),
              (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (109, 128, 151)]

screen = Screen()
screen.setup(480, 480)
t.colormode(255)
damien = Turtle()
damien.hideturtle()
y = -220

for row in range(10):
    damien.penup()
    damien.setposition(-278, y)
    for i in range(11):
        damien.dot(20, random.choice(color_list))
        damien.penup()
        damien.forward(50)
    y += 50

screen.exitonclick()
