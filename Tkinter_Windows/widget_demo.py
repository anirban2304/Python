import tkinter as tk

window = tk.Tk()

def miles_to_km():
    km = 1.66 * float(e1_value.get())
    t1.insert(tk.END, km)

b1 = tk.Button(window, text = "Execute", command = miles_to_km)
b1.grid(row = 0, column = 0)

e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

t1 = tk.Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 1)

window.mainloop()