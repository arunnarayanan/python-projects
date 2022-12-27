from tkinter import *
from tkinter import ttk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .5
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = .2
position = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time

times_dict = {'W':WORK_MIN, 'S':SHORT_BREAK_MIN, 'L':LONG_BREAK_MIN}

def start_timer():
    global position
    position += 1

    print(f'==== Current Position ==== [ {position} ]')
    if position in [1, 3, 5, 7]:
        task_lbl.config(text='WORK', fg=GREEN, bg=YELLOW)
        countdown(WORK_MIN * 60)
    elif position in [2,4,6]:
        task_lbl.config(text='BREAK', fg=YELLOW, bg="black")
        count_lbl.config(text=tick_mark * int(position/2))
        countdown(SHORT_BREAK_MIN * 60)
    elif position == 8:
        task_lbl.config(text='BREAK', fg=RED, bg=YELLOW)
        count_lbl.config(text=tick_mark * int(position / 2))
        countdown(LONG_BREAK_MIN * 60)
    else:
        print(f'Completed one full cycle. Resetting the position to 1 again')
        reset_timer()
def countdown(count):
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count-1 )
        min, sec = divmod(count, 60)
        print(f'{min:02n}:{sec:02n}')
        canvas.itemconfig(timer_text, text=f'{min:02n}:{sec:02n}')
    else:
        start_timer()

def reset_timer():
    global position
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    task_lbl.config(text='Timer', fg=GREEN)
    count_lbl.config(text='')
    position = 0


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('My Pomodoro Timer')
window.config(padx=100, pady=100, bg=YELLOW)

bg = PhotoImage(file='tomato.png')

task_lbl = Label(window, text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30), pady=10)
task_lbl.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=bg)

timer_text = canvas.create_text(100,132, text='00:00', fill='white', font=(FONT_NAME, 30, "bold"))

canvas.grid(row=1, column=1)

start_btn = Button(text='Start', font=(FONT_NAME, 14, "bold"), bg=YELLOW, highlightthickness=0)
start_btn.grid(row=2, column=0)
start_btn.config(command=start_timer)


reset_btn = Button(text='Reset', font=(FONT_NAME, 14, "bold"), bg=YELLOW, highlightthickness=0)
reset_btn.grid(row=2, column=2)
reset_btn.config(command=reset_timer)

tick_mark = '✅'

count_lbl = Label(window, text='', pady=20, bg=YELLOW)
count_lbl.grid(row=3, column=1)

window.mainloop()