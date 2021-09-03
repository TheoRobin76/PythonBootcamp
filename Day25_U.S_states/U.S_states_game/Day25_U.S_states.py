import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.speed("fastest")

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_guesses = []
score = 0

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Name a U.S State").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_guesses]
        remaining_states = pandas.DataFrame(missing_states)
        remaining_states.to_csv("remaining_states.csv")
        break

    if answer_state in states:
        state_data = data[data.state == answer_state]
        text.goto(int(state_data.x), int(state_data.y))
        text.write(answer_state)
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
        score = len(correct_guesses)

