from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters) ]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    generated_pwd = ''.join(password_list)

    # Copy password to clipboard
    pyperclip.copy(generated_pwd)
    pwd.set(generated_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = user_entry.get()
    password = pwd.get()

    if not (website and email and password):
        messagebox.showerror(title='Missing Data', message='Please ensure all fields are filled in')
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f'These are the details entered:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it OK to Save?')

    new_account_json = {
        website: {
            "email": email,
            "password": password
        }
    }

    if is_ok:
        try:
            with open('data.json', 'r') as fr:
                existing_data = json.load(fr)
        except FileNotFoundError:
            print('File not found... creating a new one...')
            with open('data.json', 'w') as fw:
                json.dump(new_account_json, fw, indent=4)
        else:
            existing_data.update(new_account_json)
            with open('data.json', 'w') as fw:
                json.dump(existing_data, fw, indent=4)
        finally:
            web_entry.delete(0, END)
            pwd.set('')


def search():
    search_site = web_entry.get()
    try:
        with open('data.json', 'r') as fr:
            existing_data = json.load(fr)
            site = existing_data.get(search_site)

            if site:
                messagebox.showinfo(title=search_site, message=f'User / Email: {site["email"]}\nPassword: {site["password"]}')
            else:
                messagebox.showwarning(title=search_site, message=f'Account doesn\'t exist!')
    except FileNotFoundError:
        print('Website not found')
        messagebox.showwarning(title=search_site, message=f'Account doesn\'t exist!')

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()

lock_img = PhotoImage(file='logo.png')
root.title('Password Manager')
root.config(padx=50, pady=50)

canvas = Canvas(root, width=200, height=200, border=1)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website
website_lbl = Label(text='Website: ')
website_lbl.grid(row=1)

web_entry = Entry(root, border=1, width=30)
web_entry.grid(row=1, column=1)
web_entry.focus()

# Search Btn
Button(text='Search', width=10, command=search).grid(row=1, column=2)

# Email / Username
user_lbl = Label(text='Email / Username: ')
user_lbl.grid(row=2)

user_entry = Entry(root, border=1, width=45)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'user@demo.com')

# Password
password_lbl = Label(text='Password: ')
password_lbl.grid(row=3)

pwd = StringVar()
password_entry = Entry(root, border=1, width=27, textvariable=pwd)
password_entry.grid(row=3, column=1)

# Generate Password Btn
password_btn = Button(text='Generate Password', command=generate_password, fg="red", bg="yellow")
password_btn.grid(row=3, column=2)

Button(text='Add', width=45, command=save).grid(row=4, column=1, columnspan=2)


root.mainloop()