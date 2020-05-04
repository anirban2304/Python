import tkinter as tk

window = tk.Tk()

def kilogram_to_units():
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462 
    ounces = float(e1_value.get())*35.274
    t1.delete("1.0", tk.END)
    t2.delete("1.0", tk.END)
    t3.delete("1.0", tk.END)
    t1.insert(tk.END, grams)
    t2.insert(tk.END, pounds)
    t3.insert(tk.END, ounces)

l1 = tk.Label(window, text = "Kg")
l1.grid(row = 0, column =0)

e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

b1 = tk.Button(window, text = "Convert", command = kilogram_to_units)
b1.grid(row = 0, column = 2)

t1 = tk.Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 0)

t2 = tk.Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 1)

t3 = tk.Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 2)

window.mainloop()