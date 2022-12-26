import tkinter
from tkinter import *
from tkinter import ttk

#Creating a new window and configurations
window = Tk()
frm = ttk.Frame(window, padding=5)
frm.grid()

window.title("Miles to KM converter")
window.minsize(width=400, height=200)

def convert_miles_to_km():
    print(f'Converting {miles_entry_text.get()} Miles to KM')
    miles = miles_entry_text.get()
    km = round(miles * 1.605, 2)
    km_entry_text.set(km)

#Labels
ttk.Label(frm, text="Miles:").grid(column=0, row=0, columnspan=2)
miles_entry_text = tkinter.DoubleVar()
miles = ttk.Entry(frm, width=20, textvariable=miles_entry_text)
miles.grid(column=2, row=0)

ttk.Label(frm, text="is equivalent to KM:").grid(column=0, row=1, columnspan=2)
km_entry_text = tkinter.IntVar()
km = ttk.Entry(frm, width=20, textvariable=km_entry_text)
km.grid(column=2, row=1)

ttk.Button(frm, text="Convert", command=convert_miles_to_km).grid(column=1,row=2)

#Buttons
window.mainloop()



