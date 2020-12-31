import tkinter as tk

greeting_count = 1

def set_message():
	global greeting_count
	label["text"] = f"Hello! ({greeting_count})"
	greeting_count += 1

root = tk.Tk()
label = tk.Label(root, text="")
button = tk.Button(root, text="Greet", command=set_message)

button.pack()
label.pack()

root.mainloop()