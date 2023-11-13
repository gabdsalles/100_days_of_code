from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
list_words = {}

#---------------LER DO ARQUIVO .CSV ---------
try:
    data = pd.read_csv("./Day 31 - Flash Card Project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./Day 31 - Flash Card Project/data/french_words.csv")
    list_words = original_data.to_dict(orient="records")
else:
    list_words = data.to_dict(orient="records")

current_card = random.choice(list_words)
french_word = current_card["French"]

def mudar_palavra():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    
    current_card = random.choice(list_words)
    french_word = current_card["French"]
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, flip_card)

#--------------FLIP CARD---------------------
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

#----------SALVAR PROGRESSO------------------

def is_known():
    list_words.remove(current_card)
    # print(len(list_words))
    data = pd.DataFrame(list_words)
    data.to_csv("./Day 31 - Flash Card Project/data/words_to_learn.csv", index=False)
    mudar_palavra()


#---------------INTERFACE--------------------

window = Tk()

window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./Day 31 - Flash Card Project/images/card_front.png")
card_back = PhotoImage(file="Day 31 - Flash Card Project/images/card_back.png")
card_bg = canvas.create_image(400, 526/2, image=card_front)
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=french_word, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./Day 31 - Flash Card Project/images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

wrong_image = PhotoImage(file="./Day 31 - Flash Card Project/images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=mudar_palavra)
button_wrong.grid(row=1, column=0)

window.mainloop()