import tkinter as tk
from tkinter import ttk
from random import choice
window = tk.Tk()
window.title("TEST SIUPY")
window.geometry("700x500")

sv = tk.StringVar(value="Some text")
sve = tk.StringVar()


def but():
    sv.set(sve.get())


label = ttk.Label(master=window, textvariable=sv)
label.pack()

entry = ttk.Entry(textvariable=sve, master=window)
entry.pack()

button = ttk.Button(master=window, text="Button", command=but)
button.pack()

exc = tk.StringVar(value="Test")
entry1 = ttk.Entry(master=window, textvariable=exc)
entry2 = ttk.Entry(master=window, textvariable=exc)
entry1.pack()
entry2.pack()
lab = ttk.Label(master=window, textvariable=exc)
lab.pack()


def rad():
    print(bolc.get())
    bolc.set(False)


bolr = tk.StringVar()
bolc = tk.BooleanVar()

radio1 = ttk.Radiobutton(variable=bolr, text="Radio A", value="A", command=rad)
radio2 = ttk.Radiobutton(variable=bolr, text="Radio B", value="B", command=rad)
radio1.pack()
radio2.pack()

check = ttk.Checkbutton(variable=bolc, text="czek", command=lambda: print(bolr.get()))
check.pack()

enbind = ttk.Entry(master=window)
enbind.pack()
enbind.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

values = ["A", "B", "C", "D"]
strung=tk.StringVar(value=values[0])
spinbox = ttk.Spinbox(values=values, master=window, textvariable=strung)
spinbox.pack()
spinbox.bind("<<Decrement>>", lambda event: print(strung.get()))

def draw(event):
    canvas.create_rectangle((event.x, event.y, event.x-5, event.y-5), fill="red", width=0)
canvas = tk.Canvas(master=window, bg="green")
canvas.bind("<B1-Motion>", lambda event: draw(event))
canvas.pack()

im=["Norbet", "Michal", "Ben", "Robert"]
na=["Gierczak", "Baron", "Masny", "Maklowicz", "Ten"]
table = ttk.Treeview(master=window, columns=("imie", "naz", "email"), show="headings")
table.heading("imie", text="Imie")
table.heading("naz", text="Nazwisko")
table.heading("email", text="Email")
table.pack()
for i in range(50):
    ime = choice(im)
    naze = choice(na)
    em = ime + naze + "@gmail.com"
    table.insert(parent="", values=(ime, naze, em), index=i)


window.mainloop()
