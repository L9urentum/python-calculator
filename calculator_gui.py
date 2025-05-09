# Name: Lawrence Nguyen
# Date: 5/8/2025
# File Purpose: Lab12

import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple GUI Calculator")

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 1, 0
for b in buttons:
    btn = tk.Button(root, text=b, font="Arial 18", padx=20, pady=20)
    btn.grid(row=row, column=col, sticky="nsew")
    btn.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i % 4, weight=1)

root.mainloop()
