from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    words_df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    print('words_to_learn.csv not found. Using the base file')
    words_df = pd.read_csv('data/french_words.csv')

words_dict_list = words_df.to_dict(orient="records")
current_word = {}

def next_card():
    global current_word, flip_timer
    root.after_cancel(id=flip_timer)
    current_word = random.choice(words_dict_list)
    print(current_word)
    canvas.itemconfigure(word_txt, text=f'{current_word["French"]}', fill="black")
    canvas.itemconfigure(lang_txt, text='French', fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = root.after(3000, flip_card)

def flip_card():
    global current_word
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfigure(word_txt, text=f'{current_word["English"]}', fill="white")
    canvas.itemconfigure(lang_txt, text='English', fill="white")

def remove_card():
    print(f'Removing {current_word} from the list')
    words_dict_list.remove(current_word)
    pd.DataFrame(words_dict_list).to_csv('data/words_to_learn.csv', index=False)
    next_card()


root = Tk()
root.title('Flashcard')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(3000, flip_card)

front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')

canvas = Canvas(root, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_img)
lang_txt = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 253, text='', font=("Ariel", 60, "bold"))
canvas.grid(row=0, columnspan=2)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_btn = Button(root, image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1)

right_img = PhotoImage(file='images/right.png')
right_btn = Button(root, image=right_img, highlightthickness=0, command=remove_card)
right_btn.grid(row=1, column=1)

next_card()

root.mainloop()