# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pwd.set('as@#asdby23')

def add():
    with open('data.txt', 'a') as f:
        website = web_entry.get()
        email = user_entry.get()
        password = pwd.get()

        f.write(website + ',' + email + ',' + password + '\n')
        web_entry.delete(0, END)
        pwd.set('')


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

root = Tk()

lock_img = PhotoImage(file='logo.png')
root.title('Password Manager')
root.config(padx=50, pady=50)

canvas = Canvas(root, width=200, height=200, border=1)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website
website_lbl = Label(text='Website')
website_lbl.grid(row=1)

web_entry = Entry(root, border=1, width=36)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

# Email / Username
user_lbl = Label(text='Email / Username')
user_lbl.grid(row=2)

user_entry = Entry(root, border=1, width=36)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'user@demo.com')

# Password
password_lbl = Label(text='Password')
password_lbl.grid(row=3)

pwd = StringVar()
password_entry = Entry(root, border=1, width=17, textvariable=pwd)
password_entry.grid(row=3, column=1)

# Generate Password Btn
password_btn = Button(text='Generate Password', command=generate_password, fg="red", bg="yellow")
password_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=34, command=add).grid(row=4, column=1, columnspan=2)


root.mainloop()