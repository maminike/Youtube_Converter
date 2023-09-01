import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x1000")
window.title("siema")

notbok = ttk.Notebook(master=window)

tab1 = ttk.Frame(master=notbok)
button = ttk.Button(master=tab1, text="robie siupe")
button.pack()

tab2 = ttk.Frame(master=notbok)
entry = ttk.Entry(master=tab2)
entry.pack()

notbok.add(tab1, text="Tab1")
notbok.add(tab2, text="tab2")
notbok.pack()


window.mainloop()
