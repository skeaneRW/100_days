import tkinter as tk
from random import randint
import pandas
#----------------------------------- constants ------------------------------------# 
BACKGROUND_COLOR = "#B1DDC6"
card_timer = None

#------------------------------ flash card functions ------------------------------#
def get_next_card():
    global current_word
    global front_img
    global card_timer
    if card_timer is not None:
        window.after_cancel(card_timer)
        card_timer = None
    try:
        with open("skeaneRW/day31/data/words_to_learn.csv","r") as file:
            file.read()
    except(FileNotFoundError, IndexError):
            reset_cards()
    finally:
        df = pandas.read_csv("skeaneRW/day31/data/words_to_learn.csv")

    if len(df) == 0:
        reset_cards()
    index = randint(0,len(df))
    current_word = df.iloc[index]
    canvas.itemconfig(card_title, text="French", fill="#000")     
    canvas.itemconfig(card_word,text=current_word["French"], fill="#000")
    canvas.itemconfig(card, image=front_img)
    card_timer = window.after(3000, func=flip_card)
    return df.iloc[index]

def reset_cards():
    all_cards = pandas.read_csv("skeaneRW/day31/data/french_words.csv")
    all_cards.to_csv("skeaneRW/day31/data/words_to_learn.csv", index=False)

def record_pass(_):
    if canvas.itemcget(card_title, "text") == "English":
        df = pandas.read_csv("skeaneRW/day31/data/words_to_learn.csv")
        print(f'I got it right. there are {len(df)} left to be learned')
        new_df = df[df['French'] != current_word["French"]]
        new_df.to_csv("skeaneRW/day31/data/words_to_learn.csv", index=False)
        print(len(new_df))
        get_next_card()

def record_fail(_):
    if canvas.itemcget(card_title, "text") == "English":
        get_next_card()

def flip_card():
    #flips card over to reveal English translation
    global back_img
    global current_word
    global card_timer
    if canvas.itemcget(card_title, "text") == "French":
        try:
            canvas.itemconfig(card_title, text="English", fill="#fff")
            canvas.itemconfig(card_word,text=current_word["English"], fill="#fff")
            canvas.itemconfig(card, image=back_img)
        except(NameError):
            get_next_card()
        else:
            card_timer = window.after(3000, func=flip_card)

    
#----------------------------------- ui layout ------------------------------------#
window = tk.Tk()
window.title("Learn French")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tk.PhotoImage(file="skeaneRW/day31/images/card_front.png")
back_img = tk.PhotoImage(file="skeaneRW/day31/images/card_back.png")
card = canvas.create_image(400,263,image=front_img)
card_title = canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400, 263,text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, sticky="WE")

pass_img = tk.PhotoImage(file="skeaneRW/day31/images/right.png")
fail_img = tk.PhotoImage(file="skeaneRW/day31/images/wrong.png")
pass_btn = tk.Label(text="pass", image=pass_img, bg=BACKGROUND_COLOR)
fail_btn = tk.Label(text="fail", image=fail_img, bg=BACKGROUND_COLOR)
pass_btn.bind("<Button-1>", record_pass)
fail_btn.bind("<Button-1>", record_fail)
fail_btn.grid(row=1, column=0)
pass_btn.grid(row=1, column=1)

get_next_card()

window.mainloop()

