import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("SIEMA")
top_frame = ttk.Frame(window)
bottom_frame = ttk.Frame(window)
bottom_frame_right = ttk.Frame(window)
label1 = ttk.Label(top_frame, text="LUBELLAS", background="red")
label2 = ttk.Label(top_frame, text="LUBELLAS", background="blue")
label3 = ttk.Label(window, text="LUBELATRON", background="green")

button1 = ttk.Button(bottom_frame, text="BUTT")
button2 = ttk.Button(bottom_frame, text="BUTT")
button3 = ttk.Button(bottom_frame, text="BUTT")
button4 = ttk.Button(bottom_frame_right, text="BUTT")
button5 = ttk.Button(bottom_frame_right, text="BUTT")
button6 = ttk.Button(bottom_frame_right, text="BUTT")
label1.pack(side="top", expand=True, fill="both")
label2.pack(side="top", expand=True, fill="both")
top_frame.pack(expand=True, fill="both")
label3.pack(expand=True)
button1.pack(fill="both", side="left", expand=True)
button2.pack(fill="both", side="left", expand=True)
button3.pack(fill="both", side="left", expand=True)

button4.pack(fill="both", expand=True)
button5.pack(fill="both", expand=True)
button6.pack(fill="both", expand=True)
bottom_frame.pack(expand=True, fill="both", side="left")
bottom_frame_right.pack(side="left", fill="both", expand=True)



window.mainloop()