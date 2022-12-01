import tkinter
from tkinter import *
from tkinter import ttk
import random

DARK_GREY = "#303841"
YELLOW = "#ffca4f"
LIGHT_GREY = "#EEEEEE"


# ---------------------------- DECISIONS SETUP ------------------------------- #
def create_decisions():
    number = int(decisions_number_entry.get())

    for n in range(0, number):
        decision_label = Label(text=f"Decision {n + 1}", bg=DARK_GREY, font=("Arial", 18))
        decision_label.grid(column=0, row=3+n)
        decision_entry= Entry()
        decision_entry.grid(column=1, row=3+n)

    pick_decision_button = Button(text="Pick", bg=DARK_GREY, command=pick_decision)
    pick_decision_button.grid(column= 1, row=3+number)

# ---------------------------- PICK A DECISION ------------------------------- #
def pick_decision():
    number = int(decisions_number_entry.get())

    choice_number = random.randint(1, number)


    decision_choice_label = Label(text=f"Go for decision #{choice_number}", bg=DARK_GREY, font=("Arial", 18))
    decision_choice_label.grid(column=0, row=number+3)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Decision Maker")
window.config(padx=100, pady=50, bg=DARK_GREY)

# image and text
canvas = Canvas(width=300, height=400, bg=DARK_GREY, highlightthickness=0)
title_text = canvas.create_text(150, 50, text="Decision Maker", fill=YELLOW, font=("Arial", 35, "bold"))
thinking_img = PhotoImage(file="thinking_emoji.png")
canvas.create_image(150, 200, image=thinking_img)
canvas.grid(column=0, row=0)

# number of decisions
decisions_number_label = Label(text="How many things are you picking between?", bg=DARK_GREY, font=("Arial", 18))
decisions_number_label.grid(column=0, row=1)

decisions_number_entry = Entry()
decisions_number_entry.grid(column=0, row=2)
decisions_number_entry.focus()

decisions_number_button = Button(text="Generate", bg=DARK_GREY, command=create_decisions)
decisions_number_button.grid(column=1, row=2)

window.mainloop()
