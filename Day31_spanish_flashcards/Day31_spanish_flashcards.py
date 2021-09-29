from random import *
from tkinter import *

import pandas
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

# ---------------------------- Functions ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Spanish1000.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text='Spanish', fill='black')
    canvas.itemconfig(card_word, text=current_card['Spanish'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(410, 266, image=card_front)
card_title = canvas.create_text(400, 150, text='Spanish', font=('Arial', 35, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Arial', 52, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, padx=50, pady=50, command=is_known)
right.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, padx=50, pady=50, command=next_card)
wrong.grid(column=0, row=1)

next_card()

window.mainloop()
