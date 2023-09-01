import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x1000")
window.title("Menu siupa")

menu = tk.Menu(master=window)
file_menu = tk.Menu(master=menu)
file_menu.add_command(label="dupa")
menu.add_cascade(label="File", menu=file_menu)
help_menu = tk.Menu(master=menu, tearoff=False)
help_menu.add_command(label="Siema")
men = tk.Menu(master=help_menu, tearoff=False)
men.add_command(label="next siups")
help_menu.add_cascade(label="Test siupy", menu=men)
menu.add_cascade(label="Help", menu=help_menu)


window.configure(menu=menu)

window.mainloop()